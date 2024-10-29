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

u_name = "Umea University"
country = "Sweden"

def get_name(prof):
    name = prof.find('div', class_='title').find('a').text.strip()
    return name

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_title(prof):
    title = prof.find('span', {"aria-hidden": "true"}).text.strip().lower()
    return title

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)

        name = future_name.result()
        link = future_link.result()
        title = future_title.result()

    if "professor" in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

        research = new_soup.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def umea_uni():
    urls = [
        "https://www.umu.se/en/department-of-computing-science/staff-at-the-department-of-computing-science/",
        "https://www.umu.se/en/staff/org/06092b7ea8ef3cfe8b9ef541d553da11d9543b45/"
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'person'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUmea University done...\n")
    return faculty_data


if __name__ == '__main__':
    umea_uni()