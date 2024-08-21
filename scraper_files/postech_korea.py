import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

u_name = "Pohang University"
country = "South Korea"

keyword_list = [
    "operating system", "robotics", "kernel", "embedded system",
    "hardware", "computer architecture", "distributed system",
    "computer organization", "vlsi", "computer and system",
    "human-computer interaction", "human computer"
]

faculty_data = []

def get_name(prof):
    name = prof.find('h3', class_="name").text.strip()
    return name

def get_email(prof):
    email = prof.find('a', string="mail").get('href')[7:] if prof.find('a', string="mail") else None
    return email

def get_link(prof):
    link = prof.find('a', string="homepage").get('href') if prof.find('a', string="homepage") else None
    return link

def get_research(prof):
    areas = prof.find('dt', class_=None, string="Areas of Interest")
    research = areas.find_next('dd').text if areas else None
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_research = executor.submit(get_research, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        print([u_name, country, name, email, link, get_scholar_profile(name)])
        faculty_data.append([u_name, name, email, link, get_scholar_profile(name)])

def postech_korea():
    url = "https://ecse.postech.ac.kr/member/professor/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="text_box")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

if __name__ == "__main__":
    postech_korea()