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

u_name = "King Fahd University of Petroleum and Minerals"
country = "Saudi Arabia"

def get_name(prof):
    name = prof.find('p', class_="card-text small").find('strong').text.strip().replace("Dr. ", "")
    return name

def get_email(prof):
    email = prof.find('a', href=re.compile(r"^mailto:")).text.strip()
    return email

def get_title(prof):
    title = prof.find('p', class_="card-text small").find('i').text.strip()
    return title

def get_link(prof, name):
    link = prof.find('a', string="Read More")['href'] if prof.find('a', string="Read More") else get_scholar_profile(name)
    return link

def get_pers_link(prof, name):
    pers_link = prof.find('i', class_="fas fa-globe").find_next('a')['href'] if prof.find('i', class_="fas fa-globe") else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_title = executor.submit(get_title, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        title = future_title.result()
        email = future_email.result()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_link = executor.submit(get_link, prof, name)
        future_pers_link = executor.submit(get_pers_link, prof, name)

        link = future_link.result()
        pers_link = future_pers_link.result()

    if "professor" or "lecturer" in title.lower():
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def kfupm():
    urls = ["https://ee.kfupm.edu.sa/people/faculty",
            "https://ics.kfupm.edu.sa/people/faculty",
            "https://coe.kfupm.edu.sa/people/faculty"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="card-body")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("King Fahd University of Petroleum and Minerals done...")
    print()
    return faculty_data


if __name__ == "__main__":
    kfupm()