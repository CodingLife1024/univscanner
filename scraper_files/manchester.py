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
    name = prof.find('a').text
    return name

def get_link(prof):
    link = prof.find('a', href=True)['href'] if prof.find('a', href=True) else "N/A"
    if link.startswith("/"):
        return "https://www.cs.manchester.ac.uk" + link
    return link

def get_email(name):
    return ".".join(name.lower().split(" ")) + "@manchester.ac.uk"

def get_expertise(prof):
    expertise = prof.text
    return expertise

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_expertise = executor.submit(get_expertise, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        expertise = future_expertise.result()

    email = get_email(name)

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research_text = new_soup.text + expertise

    found_keyword = any(re.search(re.escape(keyword), research_text, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        print([u_name, country, name, email, link, pers_link])
        faculty_data.append([u_name, country, name, email, link, pers_link])

def manchester():
    url = "https://www.cs.manchester.ac.uk/about/people/academic-and-research-staff/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    dd = soup.find('div', {'class': 'tabRows'})

    all_profs = dd.find_all('li', class_="tabrowwhite") + dd.find_all('li', class_="tabrowgrey")

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