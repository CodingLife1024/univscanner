import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "University of Manchester"
country = "England"

def get_name(prof):
    name = prof.find('div', class_="tabCol_30").text[6:]
    return name

def get_link(prof):
    link = prof.find_all('a', href=True)[0]['href'] if prof.find_all('a', href=True) else "Not Available"
    return link

def get_email(name):
    return ".".join(name.lower().split(" ")) + "@manchester.ac.uk"

def get_expertise(prof):
    expertise = prof.find_all('div', class_="tabCol_30")[2].text[19:] if len(prof.find_all('div', class_="tabCol_30")) >= 3 else "N/A"
    return expertise

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_expertise = executor.submit(get_expertise, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        expertise = future_expertise.result()

    if expertise == "Human computer systems" or expertise == "Machine learning and robotics":
        faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])
        print([u_name, country, name, email, link, get_scholar_profile(name)])

    elif expertise == "Not Available" or expertise == "Teaching":

        if link != "Not Available":
            new_r = requests.get(link, headers=headers)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            fingerprints = ""

            new_link = new_soup.find_all('button', class_="concept-badge-large dropdown-toggle")

            for i in new_link:
                fingerprints += i.text

            found_keyword = any(re.search(re.escape(keyword), fingerprints) for keyword in keyword_list)

            if found_keyword:
                faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])
                print([u_name, country, name, email, link, get_scholar_profile(name)])
        else:
            link = get_scholar_profile(name)

            if link != None:
                new_r = requests.get(link, headers=headers)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                found_keyword = any(re.search(re.escape(keyword), new_r.text) for keyword in keyword_list)
                if found_keyword:
                    faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])
                    print([u_name, country, name, email, link, get_scholar_profile(name)])

def manchester():
    url = "https://www.cs.manchester.ac.uk/about/people/academic-and-research-staff/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    dd = soup.find('div', {'class': 'tabRows'})

    all_profs = dd.find_all('li', class_=lambda x: x in ['tabrowwhite', 'tabrowgrey'])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Manchester done...\n")
    return faculty_data


if __name__ == "__main__":
    manchester()