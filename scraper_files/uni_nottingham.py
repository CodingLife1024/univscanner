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

u_name = "University of Nottingham"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('td')
    if not name:
        pass
    name = name.text.strip()
    name = name.split(',')[1] + " " + name.split(',')[0]
    return name

def get_link(prof):
    name_tag = prof.find('td')
    if not name_tag:
        pass
    link = "https://www.nottingham.ac.uk/" + name_tag.find('a')['href']
    return link

def get_email(prof):
    email = prof.find('td', class_='sys_email').find('a')['href'][7:]
    return email

def get_research(new_r):
    research = new_r.text
    return research

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

    research = new_r.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    pers_link = get_scholar_profile(name)
    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_nottingham():
    url = "https://www.nottingham.ac.uk/computerscience/people/index.aspx"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('tr')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Nottingham done...\n")
    return faculty_data

if __name__ == "__main__":
    uni_nottingham()