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

u_name = "Loughborough University"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('a').text.replace("Dr", "").replace("Professor", "").replace("Prof", "").strip()
    return name

def get_link(prof):
    link = "https://www.lboro.ac.uk" + prof.find('a')['href']
    return link

def get_title(prof):
    title = prof.find('span', class_="list__role").text.strip().lower()
    return title

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'].replace("mailto:", "")
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        title = future_title.result()
        email = future_email.result()

    if ("professor" in title or "lecturer" in title) and "emeritus" not in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research = new_soup.text
        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def loughborough_uni():
    urls = ["https://www.lboro.ac.uk/departments/compsci/staff/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('ul', class_="list list--staff").find_all('li')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nLoughborough University done...\n")
    return faculty_data

if __name__ == '__main__':
    loughborough_uni()