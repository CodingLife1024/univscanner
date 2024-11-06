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

u_name = "University of Sheffield"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('div', class_='stap-card__info').find('h3').text.strip().replace('\n', "").replace('\t', "").split(" ") if prof.find('div', class_='stap-card__info').find('h3') else "N/A"
    if name:
        name = [string for string in name if string][1:]
    name = " ".join(name)
    return name

def get_link(prof):
    name_tag = prof.find('div', class_="stap-card__info")
    link_tag = name_tag.find('a') if name_tag else None
    link = "https://www.sheffield.ac.uk" + link_tag['href'] if link_tag else "N/A"
    return link

def get_email(prof):
    email_tag = prof.find('a', href=lambda href: href and href.startswith("mailto:"))
    email = email_tag['href'][7:] if email_tag else "N/A"
    return email

def get_research(new_soup):
    research = new_soup.find('dd', class_='active').text.strip()
    return research

def get_personal_link(new_soup, name):
    pers_link = new_soup.find('a', string="Personal Website")['href'] if new_soup.find('a', string="Personal Website") else get_scholar_profile(name)
    return pers_link

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

    if link != "N/A":
        new_r = requests.get(link) if link != "N/A" else None
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit tasks for each component
            future_research = executor.submit(get_research, new_soup)
            future_personal_link = executor.submit(get_personal_link, new_soup, name)

            # Collect the results as they complete
            research = future_research.result()
            pers_link = future_personal_link.result()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_sheffield():
    url = "https://www.sheffield.ac.uk/dcs/people/academic"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    all_profs = soup.find_all('div', class_='summary-text')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Sheffield done...\n")
    return faculty_data

if __name__ == "__main__":
    uni_sheffield()