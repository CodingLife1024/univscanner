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

u_name = "University of California, Davis"
country = "United States"

def get_name(prof):
    name = prof.text.strip()
    return name

def get_link(prof):
    link = "https://cs.ucdavis.edu/" + prof.find('a')['href']
    return link

def get_email(new_soup):
    email = new_soup.find('li', class_="icon icon--link icon--envelope").find('a').text.strip()
    return email

def get_personal_link(new_soup, name):
    pers_link = new_soup.find('a', string="Personal Site")['href'] if new_soup.find('a', string="Personal Site") else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_email = executor.submit(get_email, new_soup)
        future_pers_link = executor.submit(get_personal_link, new_soup, name)

        email = future_email.result()
        pers_link = future_pers_link.result()

    faculty_data.append([u_name, country, name, email, link, pers_link])
    print([u_name, country, name, email, link, pers_link])

def uc_davis():
    urls = ["https://cs.ucdavis.edu/faculty-research/architecture",
           "https://cs.ucdavis.edu/faculty-research/database-systems",
           "https://cs.ucdavis.edu/faculty-research/human-computer-interaction"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, 'html.parser')

    super_div = soup.find_all('h3', string="Faculty")

    all_profs = []  

    for div in super_div:
        all_profs += div.find_next('div', class_="views-view-grid horizontal cols-2 clearfix").find_all('h3', class_="vm-listing__title")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of California, Davis done...\n")
    return faculty_data


if __name__ == "__main__":
    uc_davis()