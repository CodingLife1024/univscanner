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

u_name = "Politecnico di Torino"
country = "Italy"

def get_faculty_data(prof):
    name = prof.find('a').text.strip().title()
    link = "https://www.dauin.polito.it" + prof.find('a')['href']
    new_r = requests.get(link)

    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip() if new_soup.find('a', href=re.compile(r"^mailto:")) else "N/A"

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def politecnico_di_torino():
    urls = [
        "https://www.dauin.polito.it/personale/elenco",
        "https://www.det.polito.it/personale/elenco"
    ]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        all_profs += soup.find('table', {'class': 'duecolonne'}).find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPolitecnico di Torino done...\n")
    return faculty_data


if __name__ == '__main__':
    politecnico_di_torino()