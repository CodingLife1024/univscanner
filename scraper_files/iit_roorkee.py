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

u_name = "Indian Institute of Technology Roorkee (IITR)"
country = "India"

def get_faculty_data(prof):
    name = prof.find('div', class_="name").text.strip() if prof.find('div', class_="name") else "N/A"
    link = prof.find('a', string=lambda x: "READ MORE" in x).get('href') if prof.find('a', string=lambda x: "READ MORE" in x) else "N/A"
    email = prof.find('img', {"data-icon": "email"}).find_parent('div').find('div', class_="ui intro-text").text.replace("[at]", "@").strip() if prof.find('img', {"data-icon": "email"}) else "N/A"
    research = prof.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def iit_roorkee():
    urls = [
        "https://iitr.ac.in/Departments/Computer%20Science%20and%20Engineering%20Department/People/Faculty/index.html",
        "https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/People/Faculty/index.html"
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url, verify=False)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="ui faculty-card")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nIndian Institute of Technology Roorkee (IITR) done...\n")
    return faculty_data


if __name__ == '__main__':
    iit_roorkee()