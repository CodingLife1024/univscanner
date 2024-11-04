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

u_name = "Ohio State University"
country = "United States"

def get_name(prof):
    name = prof.find('span', class_='directory-grid-name').text.strip()
    return name

def get_email(prof):
    email = prof.find('div', class_='directory-grid-email').text.strip()
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        email = future_email.result()

    link = "https://cse.osu.edu/people/" + email.split('@')[0]

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    pers_link = new_soup.find('div', class_="external-website-button").find('a')['href'] if new_soup.find('div', class_="external-website-button") else get_scholar_profile(name)

    faculty_data.append([u_name, country, name, email, link, pers_link])
    print([u_name, country, name, email, link, pers_link])

def ohio_state_uni():
    urls = ["https://cse.osu.edu/research/networking-distributed-computing",
            "https://cse.osu.edu/research/systems"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")
    all_profs = soup.find_all('div', class_='layout__region layout__region--second region-large coe-widget-entity-reference-grid')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nOhio State University done...\n")
    return faculty_data


if __name__ == '__main__':
    ohio_state_uni()
