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

u_name = "Emory College of Arts and Sciences"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('h5').text.strip()
    return name

def get_link(prof):
    link = "https://computerscience.emory.edu" + prof.find('a')['href']
    return link

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:')).text if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
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

    pers_link = get_scholar_profile(name)
    faculty_data.append([u_name, country, name, email, link, pers_link])
    print([u_name, country, name, email, link, pers_link])


def emory_college():
    url = "https://computerscience.emory.edu/people/index.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="contact__details")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Emory College of Arts and Sciences done...")
    print()

    return faculty_data


if __name__ == '__main__':
    emory_college()