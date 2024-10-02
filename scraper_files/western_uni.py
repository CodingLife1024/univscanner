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

u_name = "Western University"
country = "Canada"

def get_name(prof):
    name = prof.find('div', {'class': 'infoleft'}).find('h2').text.strip()
    return name

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    return email

def get_link(prof):
    link = prof.find('a', string='Biography').get('href') if prof.find('a', string='Biography') else prof.find('a', string='External link').get('href')
    return link

def get_research(prof):
    research = prof.find('div', {'class': 'infoleft'}).text
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_research = executor.submit(get_research, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def western_uni():
    url = "https://www.csd.uwo.ca/people/faculty/index.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'teamgrid'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Western University done...")
    print()

    return faculty_data

if __name__ == '__main__':
    western_uni()
