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

u_name = "Technical University of Graz"
country = "Austria"

def get_faculty_data(prof):
    name = prof.find('span', class_="firstName").text + " " + prof.find('span', class_="lastName").text
    link = prof.find('a').get('href')

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.replace('(at)', "@").strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('th', string="Homepage").find_next('a')['href'] if new_soup.find('th', string="Homepage").find_next('a') else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def technical_uni_graz():
    urls = [
        "https://www.tugraz.at/fakultaeten/faculty-of-computer-science-and-biomedical-engineering/faculty/team/faculty"
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url, verify=False)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_=lambda x: x is not None and x.startswith("person listEntry person_"))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTechnical University of Graz done...\n")
    return faculty_data


if __name__ == '__main__':
    technical_uni_graz()