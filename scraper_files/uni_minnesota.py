import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "University of Minnesota"
country = "United States"

def get_name(prof):
    name = prof.find('div', class_="pl-item people-title").find('a').get_text().strip()
    return name

def get_link(prof):
    link = "https://cse.umn.edu" + prof.find('div', class_="pl-item people-title").find('a')['href']
    return link

def get_email(prof):
    email = prof.find('div', class_="pl-item people-email").find('a')['href'][7:] if prof.find('div', class_="pl-item people-email").find('a') else None
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    if email == None:
        return

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = new_soup.find('a', string="Personal Website")['href'] if new_soup.find('a', string="Personal Website") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_minnesota():
    url = "https://cse.umn.edu/cs/faculty-instructor-directory"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="views-row")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Minnesota done...")
    print()

    return faculty_data


if __name__ == "__main__":
    uni_minnesota()

