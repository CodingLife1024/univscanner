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

u_name = "University of California, Irvine"
country = "United States"

def get_name(prof):
    name = prof.find('h3').text.strip()
    return name

def get_email(prof):
    email = prof.find('a', href=re.compile(r"^mailto:")).text.strip()
    return email

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    pers_link = new_soup.find('a', class_="person__link c-text-btn")['href'] if new_soup.find('a', class_="person__link c-text-btn") else get_scholar_profile(name)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uc_irvine():
    urls = ["https://cs.ics.uci.edu/faculty/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    super_class = soup.find_all('div', "s-content people-panel__container")[:2]

    all_profs = []

    for i in super_class:
        profs = i.find_all('article', class_="item--person")
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of California, Irvine done...\n")
    return faculty_data

if __name__ == '__main__':
    uc_irvine()