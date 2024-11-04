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

u_name = "Novosibirsk State University"
country = "Russia"

def get_name(prof):
    name = prof.find('a').text.replace("Dr", "").replace("Prof", "").replace("Professor", "").strip()
    return name

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'].replace("mailto:", "") if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
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
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def novisibirsk_state_uni():
    urls = ["https://pure.nsu.ru/portal/en/persons/search.html?search=&organisationName=Department%20of%20Information%20Technologies&journalName=&organisations=3086172&uri=&pageSize=all&page=0"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, 'html.parser')

    all_profs = soup.find_all('li', {'class': 'portal_list_item'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNovosibirsk State University done...\n")
    return faculty_data


if __name__ == "__main__":
    novisibirsk_state_uni()