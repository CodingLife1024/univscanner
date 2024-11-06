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

u_name = "University of Groningen"
country = "Netherlands"

def get_name(prof):
    name = prof.find('div', {'class':'rug-h3'}).find('a').get_text().strip()
    return name

def get_link(prof):
    link = "https://www.rug.nl" + prof.find('div', {'class':'rug-h3'}).find('a')['href']
    return link

def get_email(prof):
    email = prof.find('span', {'class':"js--decode"}).get_text().replace(" ", "@")
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

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    pers_link_tag = new_soup.find('div', class_="rug-layout__item rug-width-m-6-24 rug-attributes__label", string=None).find_next('div').find('a')

    pers_link = pers_link_tag['href'] if pers_link_tag and pers_link_tag.get('href') else get_scholar_profile(name)

    faculty_data.append([u_name, country, name, email, link, pers_link])
    print([u_name, country, name, email, link, pers_link])


def uni_groningen():
    urls = ["https://www.rug.nl/about-ug/practical-matters/find-an-expert?discipline=Computer+Science%2C+Hardware+%26+Architecture",
            "https://www.rug.nl/about-ug/practical-matters/find-an-expert?discipline=Computer+Science%2C+Software+Engineering"]

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class':'rug-pv-s rug-ph-xs'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniverseity of Groningen done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_groningen()