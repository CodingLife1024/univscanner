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

u_name = "University of Otago"
country = "New Zealand"

def get_name(prof):
    name = prof.find('a', class_="grid-card__link").text.strip()
    return name

def get_email(prof):
    email_tag = prof.find('a', href=re.compile(r"^mailto:"))
    email = email_tag['href'].replace("mailto:", "") if email_tag else "N/A"
    return email

def get_link(prof):
    link = prof.find('a', class_="grid-card__link")['href']
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

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_otago():
    url = "https://www.otago.ac.nz/school-of-computing/our-people"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the first 6 'div' elements inside <main> with no class
    super_class = soup.find("main", class_="content").find_all('div', class_="template template-margin-top--medium template-margin-bottom--medium")[:6]

    all_profs = []

    for i in super_class:
        profs = i.find_all('div', class_="grid-card__contents")
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Otago done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_otago()