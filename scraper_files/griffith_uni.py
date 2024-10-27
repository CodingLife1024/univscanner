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

u_name = "Griffith University"
country = "Australia"

def get_faculty_data(prof):
    name = prof.find('a').text.replace('Dr', "").replace('Professor', "").replace('\xa0', " ").replace('Associate', "").replace('Mr', "").strip()
    link = prof.find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.content, 'html.parser')

    email = new_soup.find('a', href=re.compile(r'mailto:')).text if new_soup.find('a', href=re.compile(r'mailto:')) else "N/A"

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword or True:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def griffith_uni():
    urls = [
        "https://www.griffith.edu.au/griffith-sciences/school-information-communication-technology/our-staff",
        "https://www.griffith.edu.au/griffith-sciences/school-engineering-built-environment/our-staff",
    ]

    # for url 1

    r = requests.get(urls[0])
    soup = BeautifulSoup(r.content, 'html.parser')

    super_class = soup.find_all('ul', class_="feature")[:3]

    all_profs = []

    for i in super_class:
        profs = i.find_all('li')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 2
    r = requests.get(urls[1])
    soup = BeautifulSoup(r.content, 'html.parser')

    super_class = soup.find_all('div', class_="gu4")[:3]

    all_profs = []

    for i in super_class:
        profs = i.find_all('li')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nGriffith University - School of Information and Communication Technology done...\n")
    return faculty_data


if __name__ == '__main__':
    griffith_uni()