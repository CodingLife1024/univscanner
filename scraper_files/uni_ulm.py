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

u_name = "Universitat Ulm"
country = "Germany"

def get_faculty_data(prof):
    name_string = prof.text.strip()
    name = name_string.split(".")[-1].strip()
    link = "https://www.uni-ulm.de" + prof['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r'^mailto:'))['href'] if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_ulm():
    urls = [
        "https://www.uni-ulm.de/en/in/fakultaet/fakultaet/fakultaet-organisation/",
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('div', {'class': 'row gx-0'}).find_all('a')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversitat Ulm done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_ulm()