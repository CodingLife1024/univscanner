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

u_name = "Macquarie University"
country = "Australia"

def get_name(prof):
    name = prof.find('a').text.replace("Dr ", "").strip()
    return name

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_research(prof):
    research = prof.find('ul').text.strip()
    return research

def get_email(prof):
    email = prof.find('a', href=re.compile(r"^mailto:"))['href'].replace("mailto:", "")
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_research = executor.submit(get_research, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        research = future_research.result()
        email = future_email.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def macquarie_uni():
    urls = ["https://www.mq.edu.au/faculty-of-science-and-engineering/departments-and-schools/school-of-computing/our-people"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    super_class = soup.find_all('tbody')[1:3]

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Macquarie University done...")
    print()
    return faculty_data

if __name__ == '__main__':
    macquarie_uni()