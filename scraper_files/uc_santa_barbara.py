import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "University of California, Santa Barbara"
country = "United States"

def get_name(prof):
    name = prof.find('h2').get_text().strip()
    return name

def get_link(prof):
    link = "https://www.cs.ucsb.edu" + prof.find('a')['href']
    return link

def get_email(prof):
    email = prof.find('a', href=lambda x: x and x.startswith("mailto:")).get_text() if prof.find('a', href=lambda x: x and x.startswith("mailto:")) else "N/A"
    return email

def get_pers_link(prof, name):
    pers_link = prof.find('a', string="Personal Website")['href'] if prof.find('a', string="Personal Website") else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    pers_link = get_pers_link(prof, name)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.find('div', class_="field field--name-field-bio field--type-text-long field--label-above").get_text() if new_soup.find('div', class_="field field--name-field-bio field--type-text-long field--label-above") else "N/A"

    research_2 = new_soup.find('div', class_="research-description").get_text() if new_soup.find('div', class_="research-description") else "N/A"

    research = research + research_2

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword or True:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uc_santa_barbara():
    url = "https://www.cs.ucsb.edu/people/faculty"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('div', class_="view-content").find_all('span', class_="field-content")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of California Santa Barbara done...\n")
    return faculty_data



if __name__ == "__main__":
    uc_santa_barbara()
