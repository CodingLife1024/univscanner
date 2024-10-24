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

u_name = "King Saud University"
country = "Saudi Arabia"

def get_faculty_data_1(prof):
    columns = prof.find_all('td')
    name = columns[0].text.replace("Prof.", "").replace("Dr.", "").strip()
    link = columns[0].find('a').get('href')
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'].split(":")[-1] if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    columns = prof.find_all('td')
    name = columns[0].text.replace("Prof.", "").strip()
    link = columns[0].find('a').get('href')

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text
    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def king_saud_uni():
    urls = [
        "https://cs.ksu.edu.sa/en/cs/faculty-and-staff",
        "https://ccis.ksu.edu.sa/en/it/it-faculty-and-staff",
        "https://ccis.ksu.edu.sa/en/ce/faculty-and-staff",
        "https://ccis.ksu.edu.sa/en/node/773",
        "https://ccis.ksu.edu.sa/en/node/891",
    ]

    # for url 1

    r = requests.get(urls[0], verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')[:-1]

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 2

    r = requests.get(urls[1], verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')[:-1]

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 3

    r = requests.get(urls[2], verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')[:-1]

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 4

    r = requests.get(urls[3], verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')[:-1]

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 5

    r = requests.get(urls[4], verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')[:-1]

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nKing Saud University done...\n")
    return faculty_data


if __name__ == '__main__':
    king_saud_uni()