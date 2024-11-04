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

u_name = "Queen Mary University of London"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('h3').text
    return name

def get_email(prof):
    email = prof.find('a', href=lambda href: href and href.startswith('mailto:')).text if prof.find('a', href=lambda href: href and href.startswith('mailto:')) else None
    return email

def get_link(prof):
    link = "https://www.qmul.ac.uk" + prof.find('a')['href'] if prof.find('a') else None
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

    if not link or not email:
        return

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')
    research = new_r.text
    email_link = new_soup.find('a', href=lambda href: href and href.startswith('mailto:'))

    pers_link = ""

    if email_link:
        pers_link = email_link.find_next('a')['href'] if email_link.find_next('a') else get_scholar_profile(name)
        if pers_link[0] == "#":
            pers_link = get_scholar_profile(name)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def queen_mary_uni():
    url = "https://www.qmul.ac.uk/eecs/people/academic/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('div', class_='profiles two-column-profiles cd-gallery').find_next('ul').find_all('li')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nQueen Mary University of London done...\n")
    return faculty_data

if __name__ == '__main__':
    queen_mary_uni()
