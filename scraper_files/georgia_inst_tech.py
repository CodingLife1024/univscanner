import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

u_name = "Georgia Institute of Technology"
country = "United States"

faculty_list = []

def get_name(prof):
    return prof.find('h2', class_=None).text.strip()

def get_link(prof):
    link = prof.find('a', string="Personal Webpage").get('href')
    return link

def get_email(prof):
    link = get_link(prof)
    return str(link).split('/')[-2][1:] + "@gatech.edu"

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

    pers_link = get_scholar_profile(name)

    faculty_list.append([u_name, country, name, email, link, pers_link])
    print([u_name, country, name, email, link, pers_link])

def georgia_inst_tech():
    url1 = "https://www.scs.gatech.edu/data-systems-and-analytics"
    url2 = "https://www.scs.gatech.edu/computer-architecture"
    url3 = "https://www.scs.gatech.edu/systems"

    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)

    soup = BeautifulSoup(response1.text + response2.text + response3.text, 'html.parser')

    all_profs = soup.find_all('div', class_="page-title-large my-3 clearfix block block-layout-builder block-inline-blockbasic")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nGeorgia Institute of Technology done...\n")
    return faculty_list


if __name__ == '__main__':
    georgia_inst_tech()