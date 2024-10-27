import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint
import base64

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Aalborg University"
country = "Denmark"

def get_name(prof):
    name = prof.find('h3').text.strip()
    return name

def get_link(prof):
    link = "https://vbn.aau.dk" + prof.find('a')['href']
    return link

def get_email(prof):
    email = base64.b64decode(prof.find('a', class_="email")['data-md5']).decode('utf-8')[7:]
    return email

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

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword or True:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def aalborg_uni():
    urls = [
        "https://vbn.aau.dk/en/organisations/institut-for-datalogi/persons/",
        "https://vbn.aau.dk/en/organisations/institut-for-datalogi/persons/?page=1",
        "https://vbn.aau.dk/en/organisations/institut-for-datalogi/persons/?page=2",
        "https://vbn.aau.dk/en/organisations/institut-for-datalogi/persons/?page=3",
        "https://vbn.aau.dk/en/organisations/institut-for-datalogi/persons/?page=4",
        "https://vbn.aau.dk/en/organisations/institut-for-datalogi/persons/?page=5",
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        print("Fetching..." + url + "\n")
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'result-container'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nAalborg University done...\n")
    return faculty_data


if __name__ == '__main__':
    aalborg_uni()