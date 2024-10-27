import concurrent.futures
import os
import pprint
import re
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import keyword_list
from components.google_scholar import get_scholar_profile

faculty_data = []

u_name = "University of Tasmania"
country = "Australia"

def get_faculty_data(prof):
    columns = prof.find_all('td')

    name = columns[1].find('a').text.replace("Dr", "").replace("Professor", "").replace("Associate", "").strip()
    link = columns[1].find('a')['href']
    email = columns[2].find('a').text.strip()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research =new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_tasmania():
    urls = [
        "https://www.utas.edu.au/built-digital-natural/people/information-and-communication-technology?queries_classification_query=Academic",
        "https://www.utas.edu.au/built-digital-natural/people/information-and-communication-technology?queries_classification_query=Academic&result_1044714_result_page=2"
    ]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        print("Fetching..." + url + "\n")
        all_profs += soup.find('tbody').find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Tasmania done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_tasmania()