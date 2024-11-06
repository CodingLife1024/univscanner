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

u_name = "University of Southampton"
country = "United Kingdom"

def get_name(prof):
    name_tag = prof.find('a', class_="font-bold text-2xl text-endeavour")
    if name_tag:
        span_tag = name_tag.find('span')
        if span_tag:
            span_tag.extract()
        name = name_tag.text.strip()
        name = " ".join(name.split(" ")[1:])
        return name

def get_link(prof):
    name_tag = prof.find('a', class_="font-bold text-2xl text-endeavour")
    if name_tag:
        link = name_tag['href']
        return link

def get_email(prof):
    email_tag = prof.find('a', class_="link-base")
    if email_tag:
        email = email_tag.text.strip()
        return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

        print([u_name, country, name, email, link, get_scholar_profile(name)])
        faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])

def uni_southampton():
    url = "https://www.southampton.ac.uk/research/groups/computational-engineering-design-group"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='person-teaser')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Southampton done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_southampton()

