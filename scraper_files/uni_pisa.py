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

u_name = "Universita di Pisa"
country = "Italy"

def get_faculty_data(prof):
    columns = prof.find_all('td')

    name = columns[1].text.strip() + " " + columns[0].text.strip()
    email_parts = columns[2].find('a')
    email = email_parts['data-name'] + "@" + email_parts['data-domain'] + "." + email_parts['data-tld']
    link = columns[3].find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_pisa():
    url = "https://di.unipi.it/en/people/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = []

    super_class = soup.find_all('table', class_="tel table table-sm table-striped table-bordered")[:3]

    for i in super_class:
        profs = i.find_all('tr')
        all_profs += profs

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversita di Pisa done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_pisa()