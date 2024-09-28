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

u_name = "University of Technology Malaysia"
country = "Malaysia"

def get_name(prof):
    name = prof.find_next('h5').text.strip().replace("Dr. ", "")
    return name

def get_email(prof):
    email = prof.find_next('a', href=re.compile(r"^mailto:")).text.strip()
    return email

def get_link(prof):
    link = prof.find_next('h5').find('a')['href']
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

    pers_link = new_soup.find('a', string="View CV")['href'] if new_soup.find('a', string="View CV") else get_scholar_profile(name)

    pers_r = requests.get(pers_link)
    pers_soup = BeautifulSoup(pers_r.text, "html.parser")
    research = pers_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_tech_malaysia():
    urls = ["https://fsktm.um.edu.my/department-of-information-systems",
            "https://fsktm.um.edu.my/department-of-computer-system-amp-technology",
            "https://fsktm.um.edu.my/department-of-software-engineering",
            "https://fsktm.um.edu.my/department-of-artificial-intelligence"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="col-lg-3")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Technology Malaysia done...")
    print()
    return faculty_data

if __name__ == "__main__":
    uni_tech_malaysia()