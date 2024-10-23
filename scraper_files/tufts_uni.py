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

u_name = "Tufts University"
country = "United States"

def get_name(prof):
    name = prof.find('span', class_='person__text person__name-link').text.strip()
    return name

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'][7:] if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    return email

def get_link(prof):
    link = prof.find('a', string='Department Profile').get('href')
    return link

def get_title(prof):
    title = prof.find('div', {'class': 'mb-3 person-title'}).text.lower()
    return title

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_title = executor.submit(get_title, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        title = future_title.result()

    research = prof.text

    if ("professor" in title or "lecturer" in title) and "emeritus" not in title:

        try:
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, 'html.parser')

            research += new_soup.text
        except:
            pass

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = prof.find('i', class_="bi bi-person-fill faculty-icon").find_next('a')['href'] if prof.find('i', class_="bi bi-person-fill faculty-icon") else get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def tufts_uni():
    urls = [
        "https://engineering.tufts.edu/people/faculty",
        "https://engineering.tufts.edu/people/faculty?title=&department=All&category=All&page=1",
        "https://engineering.tufts.edu/people/faculty?title=&department=All&category=All&page=2",
        "https://engineering.tufts.edu/people/faculty?title=&department=All&category=All&page=3",
        "https://engineering.tufts.edu/people/faculty?title=&department=All&category=All&page=4",
        "https://engineering.tufts.edu/people/faculty?title=&department=All&category=All&page=5",
        "https://engineering.tufts.edu/people/faculty?title=&department=All&category=All&page=6",
        "https://engineering.tufts.edu/people/faculty?title=&department=All&category=All&page=7"
    ]

    total_text = ""

    for url in urls:
        print(f"Fetching {url}...\n")
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, 'html.parser')

    all_profs = soup.find_all("div", class_="col faculty-grid__col")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTufts University done...\n")
    return faculty_data


if __name__ == "__main__":
    tufts_uni()