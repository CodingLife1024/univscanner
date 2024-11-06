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

u_name = "University of Bern"
country = "Switzerland"

def get_name(left_side):
    name_tag = left_side.find('dd')
    if name_tag:
        name = name_tag.get_text(strip=True)
    else:
        name = "N/A"
    return name

def get_email(left_side):
    email_tag = left_side.find('dd', class_="mail").find('a')
    if email_tag:
        email = email_tag['href'].replace('javascript:window.location.href=\'mailto:\'+atob(\'', '').replace('\')', '')
        email = re.sub(r'[^\w@.]', '', email)
    else:
        email = "N/A"
    return email

def get_link(left_side):
    link_tag = left_side.find('a')
    if link_tag:
        link = link_tag['href']
    else:
        link = "N/A"
    return link

def get_faculty_data(prof):
    left_side = prof.find('dl', class_="left")
    right_side = prof.find('dl', class_="right")

    if not left_side or not right_side:
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, left_side)
        future_email = executor.submit(get_email, left_side)
        future_link = executor.submit(get_link, left_side)

        # Collect the results as they complete
        name = future_name.result()
        email = future_email.result()
        link = future_link.result()

    new_r = requests.get(link)
    research = new_r.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        print([u_name, country, name, email, link, pers_link])
        faculty_data.append([u_name, country, name, email, link, pers_link])

def uni_bern():
    url = "https://www.inf.unibe.ch/about_us/people/index_eng.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('article', class_="team-box")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Bern done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_bern()
