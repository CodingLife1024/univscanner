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

u_name = "University of Twente"
country = "Netherlands"

def get_faculty_data(prof):
    name = prof.get_text().replace('dr.', "").replace('ir.', "").replace('prof', '').strip()
    link = prof.get('href')

    new_r = requests.get(link + "?tab=education")
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip()
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_twente():
    urls = ["https://www.utwente.nl/en/eemcs/caes/people/"]

    total_text = ""
    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    super_class = soup.find_all('div', class_='peopleoverview__summary__category')[:4]

    all_profs = []

    for i in super_class:
        all_profs.extend(i.find_all('a'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Twente done...")
    print()
    return faculty_data

if __name__ == "__main__":
    uni_twente()