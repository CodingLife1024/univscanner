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

u_name = "Cardiff University"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('h2', class_="profile-title fn").text.strip()
    name = name.replace("Dr ", "").replace("Prof ", "").replace("Mr ", "").replace("Ms ", "").replace("Mrs ", "").replace("Miss ", "").replace("Professor", "")
    return name

def get_link(prof):
    link = prof.find('h2').find('a')['href'] if prof.find('h2').find('a') else "N/A"
    return link

def get_title(prof):
    title = prof.find('p', class_="profile-subtitle").text.strip().lower()
    return title

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:')).text if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    return email


def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        title = future_title.result()
        email = future_email.result()

    if "professor" in title or "lecturer" in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text
        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def cardiff_uni():
    url = "https://www.cardiff.ac.uk/computer-science/people/academic-and-research-staff"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="profile with-image vcard")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Cardiff University done...")
    print()
    return faculty_data


if __name__ == '__main__':
    cardiff_uni()