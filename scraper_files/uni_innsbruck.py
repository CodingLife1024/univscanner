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

u_name = "Universitat Innsbruck"
country = "Austria"

def get_faculty_data_1(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip()
    email = columns[1].find('a')['href'].split(':')[-1]
    link = columns[3].find('a')['href'] if columns[3].find('a') else "N/A"

    new_r = requests.get(link)
    research = new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip()
    link = columns[0].find('a')['href']
    email = columns[2].find('a')['href'].split(':')[-1]

    if not link.startswith('https://'):
        link = 'https://www.uibk.ac.at/mathematik/personal/' + link


    new_r = requests.get(link)
    research = new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_innsbruck():
    urls = [
        "https://www.uibk.ac.at/informatik/team/",
        "https://www.uibk.ac.at/mathematik/personal/"
        ]

    # for url 1

    r = requests.get(urls[0])
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')

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

    all_profs = soup.find('tbody').find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print('\nUniversity of Innsbruck done...\n')
    return faculty_data


if __name__ == '__main__':
    uni_innsbruck()
