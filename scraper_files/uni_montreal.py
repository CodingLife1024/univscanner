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

u_name = "University of Montreal"
country = "Canada"

def get_name(prof):
    first_name = prof.find('span', class_="prenom").text.strip()
    last_name = prof.find('span', class_="nom").text.strip()
    name = first_name + " " + last_name
    return name

def get_email(prof):
    email = prof.find('div', class_="courriel").text.strip() if prof.find('div', class_="courriel") else "N/A"
    return email

def get_link(prof):
    anchor_tag = prof.find('a')
    link = "https://diro.umontreal.ca" + anchor_tag['href'] if anchor_tag else "N/A"
    return link

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

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    research = new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = new_soup.find('p', class_="presenceWeb_link")['href'] if new_soup.find('p', class_="presenceWeb_link") else get_scholar_profile(name)

        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_montreal():
    url = "https://diro.umontreal.ca/english/departement-directory/professors/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('div', class_='individu with-affiliations with-expertises')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Montreal done...\n")
    return faculty_data

if __name__ == "__main__":
    uni_montreal()