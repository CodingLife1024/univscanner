import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import html

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "University of Pittsburgh"
country = "United States"

def get_name(prof):
    name = prof.find('span', class_="field-content view-people__title").get_text().strip()
    return name

def get_link(prof):
    link = "https://www.cs.pitt.edu" + prof.find('a')['href']
    return link

def get_email(prof):
    script_content = prof.find_next('div', class_="views-field views-field-field-email").find('script').string
    obfuscated_email = re.search(r'href="(.*?)"', script_content).group(1)
    decoded_email = html.unescape(obfuscated_email)
    email = decoded_email.replace('mailto:', '')
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

    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = new_soup.find('a', string="Personal webpage")['href'] if new_soup.find('a', string="Personal Webpage") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_pittsburgh():
    url = "https://www.cs.pitt.edu/people"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('div', class_="group").find_all('div', class_="views-field views-field-field-person-img view-people__person-img")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Pittsburgh done...")
    print()

    return faculty_data


if __name__ == '__main__':
    uni_pittsburgh()