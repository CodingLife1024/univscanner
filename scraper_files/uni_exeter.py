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

u_name = "University of Exeter"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('a').get_text().replace("Dr ", "").replace(".", "").strip()
    return name

def get_link(prof):
    link = "https://computerscience.exeter.ac.uk/people" + prof.find('a')['href'].replace("..", "")
    return link

def get_email(new_soup):
    email = new_soup.find('a', href=re.compile(r'^mailto:')).get_text().strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"
    return email

def get_research(new_soup):
    research = new_soup.find('div', id="overview").text if new_soup.find('div', id="overview") else "N/A"
    return research


def get_faculty_data(prof):
    name = prof.find('a').text.replace("Dr", "").replace("Professor", "").replace("Ms", "").strip()
    link = prof.find('a')['href']
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'][7:] if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    title = prof.find('p').text.strip().lower()

    if "lecturer" in title or "professor" in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = new_soup.find('a', class_="button arrow-icon")['href'] if new_soup.find('a', class_="button arrow-icon") else get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def uni_exeter():
    urls = [
        "https://computerscience.exeter.ac.uk/people/academic/",
        "https://engineering.exeter.ac.uk/people/academicstaff/"
    ]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        all_profs += soup.find_all('div', class_="profile-card-listing row")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Exeter done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_exeter()