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

u_name = "University of Glasgow"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('a').text.strip()
    name_parts = name.split(',')
    name = name_parts[1] + " " + name_parts[0]
    name = " ".join(name.split(" ")[1:])
    return name

def get_link(prof):
    base_url = "https://www.gla.ac.uk/schools/computing/staff/"
    link = base_url + prof.find('a').get('href')
    return link

def get_email(prof):
    link = get_link(prof)
    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    email = new_soup.find('span', itemprop_="email").text.strip() if new_soup.find('span', itemprop_="email") else None
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        # Collect results
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    print([u_name, country, name, email, link, get_scholar_profile(name)])
    faculty_data.append([u_name, country, name, email, link, get_scholar_profile(name)])

def uni_glasgow():
    base_url = "https://www.gla.ac.uk/schools/computing/staff/"
    url = base_url + "#research%26teaching"

    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")
    prof_list = soup.find('ul', id="research-teachinglist", class_="longlist jquerylist")

    if not prof_list:
        print("Error: Could not find professor list.")
        return

    all_profs = prof_list.find_all('li')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Glasgow done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_glasgow()
