import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

u_name = "Utrecht University"
country = "Netherlands"

faculty_data = []

def get_name(prof):
    name = prof.find('h3', class_="profile__name").text.strip()
    return name

def get_email(prof):
    email = prof.find('div', class_="profile__email").find('a')['href'][7:]
    return email

def get_link(prof):
    link = prof.find('h3', class_="profile__name").find('a')['href']
    return link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    pers_link = get_scholar_profile(name)
    if [u_name, country, name, email, link, pers_link] not in faculty_data:
        print([u_name, country, name, email, link, pers_link])
        faculty_data.append([u_name, country, name, email, link, pers_link])

def utrecht_uni():
    urls = ["https://www.uu.nl/en/research/institute-of-information-and-computing-sciences",
            "https://www.uu.nl/en/research/software",
            "https://www.uu.nl/en/research/interaction"]

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_='profile')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Utrecht University done...")
    print()
    return faculty_data


if __name__ == '__main__':
    utrecht_uni()