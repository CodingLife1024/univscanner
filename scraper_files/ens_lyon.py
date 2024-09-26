import requests
from bs4 import BeautifulSoup
import concurrent.futures
import sys
import os
import re


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer", "concurrency"]

faculty_data = []

u_name = "University of Lyon"
country = "France"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].get_text().strip()
    link = "https://informatique.ens-lyon.fr" + columns[0].find('a')['href']
    research = columns[1].get_text().strip()
    email = columns[2].get_text().strip().replace(" [a] ", "@").replace(" [point] ", ".")

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def ens_lyon():
    url = "https://informatique.ens-lyon.fr/en/team/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Lyon done...")
    print()

    return faculty_data

if __name__ == '__main__':
    ens_lyon()
