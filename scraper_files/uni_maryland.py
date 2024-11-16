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

u_name = "University of Maryland"
country = "United States"

def get_name(prof):
    name = prof.find('div', class_="media-body").find('a').get_text().strip()
    return name

def get_link(prof):
    link = "https://www.cs.umd.edu" + prof.find('div', class_="media-body").find('a')['href']
    return link

def get_research(prof):
    research = prof.text
    return research

def get_email(new_soup):
    email = new_soup.find('strong', string="Email: ").find_next('a')['href'] if new_soup.find('strong', string="Email: ") else "N/A"
    return email

def get_pers_link(new_soup, name):
    pers_link = new_soup.find('strong', string="Website: ").find_next('a').get_text().strip() if new_soup.find('strong', string="Website: ") else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_research = executor.submit(get_research, prof)

        name = future_name.result()
        link = future_link.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_email = executor.submit(get_email, new_soup)
            future_pers_link = executor.submit(get_pers_link, new_soup, name)

            email = future_email.result()
            pers_link = future_pers_link.result()

        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_maryland():
    url = "https://www.cs.umd.edu/people/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('span', class_="field-content")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Maryland done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_maryland()