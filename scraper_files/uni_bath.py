import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint
import unidecode

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []


u_name = "University of Bath"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('a').get_text().replace("Dr ", "").replace("Professor", "").strip()
    return unidecode.unidecode(name)

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    email = new_soup.find('a', class_="email").get_text().strip() + "@bath.ac.uk" if new_soup.find('a', class_="email") else "N/A"
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_bath():
    url = "https://www.bath.ac.uk/teams/department-of-computer-science-academic-staff/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('div', class_="md-ruled-list")
    all_profs = []
    for i in super_class:
        profs = i.find_all('li')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Bath done...")
    print()

    print("\nUniversity of Bath done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_bath()
