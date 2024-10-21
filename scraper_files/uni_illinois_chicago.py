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

u_name = "University of Illinois Chicago"
country = "United States"

def get_name(prof):
    name_parts = prof.find('span', class_="_name").text.strip().replace("\n", "").replace(" ", "").split(",")
    name = name_parts[1] + " " + name_parts[0]
    return name

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    return email

def get_link(prof):
    link = prof.find('span', class_="_name").find('a').get('href')
    return link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('h2', class_="_label", string="Related Sites:").find_next('a')['href'] if new_soup.find('h2', class_="_label", string="Related Sites:") and new_soup.find('h2', class_="_label", string="Related Sites:").find_next('a') else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_illinois_chicago():
    urls = [
        "https://cs.uic.edu/faculty-staff/faculty/"
        ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        print("Scraping: ", url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('article', {'class':"profile-teaser"})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Illinois Chicago done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_illinois_chicago()