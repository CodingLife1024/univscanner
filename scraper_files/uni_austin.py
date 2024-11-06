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

u_name = "University of Texas at Austin"
country = "United States"

def extract_email(new_soup):
    email_elem = new_soup.find('div', class_="contact-field contact-email")
    email = email_elem.text if email_elem else None
    return email

def extract_website(new_soup, name):
    pers_link = new_soup.find('a', string='Homepage')['href'] if new_soup.find('a', string='Homepage') else get_scholar_profile(name)
    return pers_link

def get_link(prof, name):
    name_tag = prof.find('div', class_='views-field views-field-title').find('span', class_='field-content').find('a')
    return "https://www.cs.utexas.edu" + name_tag['href']


def get_faculty_data(prof):
    name_tag = prof.find('div', class_='views-field views-field-title').find('span', class_='field-content').find('a')
    name = name_tag.text.strip()
    link = "https://www.cs.utexas.edu" + name_tag['href']

    # Extract research groups
    research_groups = []
    research_group_tags = prof.find('div', class_='views-field views-field-field-research-groups').find_all('a')
    for group_tag in research_group_tags:
        research_groups.append(group_tag.text.strip())

    research = ", ".join(research_groups) if research_groups else "Research groups not found"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    # Fetch the Google Scholar profile
    if found_keyword:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_email = executor.submit(extract_email, new_soup)
            future_website = executor.submit(extract_website, new_soup, name)

            email = future_email.result()
            pers_link = future_website.result()

        if email:
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def uni_austin():
    url = "https://www.cs.utexas.edu/people"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    faculty_divs = soup.find_all('div', class_='views-row')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in faculty_divs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Ensure exceptions are raised
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Texas at Austin done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_austin()
