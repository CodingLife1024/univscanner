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

u_name = "Virginia Polytechnic Institute and State University"
country = "United Kingdom"

def get_faculty_data(prof):
    name = prof.find('a').text.replace("\n", "").replace(", bio", "").replace(", redirect", "").strip()
    link = prof.find('a').get('href')

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def virginia_tech():
    urls = [
        "https://website.cs.vt.edu/people/faculty.html",
        "https://ece.vt.edu/people/faculty.html"
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'vt-list-item-col col-sm-12 col-md-8 col-12'})
    all_profs_2 = soup.find_all('div', {'class': 'vt-list-item-col col-sm-12 col-md-6 col-12'})[1:-1:2]

    all_profs.extend(all_profs_2)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nVirginia Polytechnic Institute and State University done...\n")
    return faculty_data


if __name__ == '__main__':
    virginia_tech()