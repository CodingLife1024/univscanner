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

u_name = "University of Southern Denmark"
country = "Denmark"

def get_faculty_data_1(prof):
    name = prof.find('a').text.strip()
    link = prof.find('a')['href']
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip() + " " + columns[1].text.strip()
    link = columns[0].find('a')['href']
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'][7:] if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_southern_denmark():
    urls = [
        "https://www.sdu.dk/en/om-sdu/institutter-centre/imada_matematik_og_datalogi/medarbejdere/videnskabeligt-personale",
        "https://www.sdu.dk/en/om-sdu/institutter-centre/ime-mekanik-elektronik/medarbejdere"
    ]

    # for url 1

    r = requests.get(urls[0])
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'employee-list__card__text'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 2

    r = requests.get(urls[1])
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = []

    super_class = soup.find_all('tbody', class_="list")

    for i in super_class:
        all_profs.extend(i.find_all('tr'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Southern Denmark done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_southern_denmark()
