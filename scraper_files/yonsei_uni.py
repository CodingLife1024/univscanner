import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

u_uname = "Yonsei University"
country = "South Korea"

faculty_data = []

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

def get_name(prof):
    name = prof.find('dt').text.strip()
    return name

def get_link(prof):
    link_tag = prof.find('a', class_='board-faculty-shortcut')
    link = link_tag['href'] if link_tag else "Link not available"
    return "https://devcms.yonsei.ac.kr" + link

def get_email(prof):
    email_tag = prof.find('a', href=True)
    email = email_tag.text.strip() if email_tag else "Email not available"
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

    # Store the data
    faculty_data.append([u_uname, country, name, email, link, get_scholar_profile(name)])
    print([u_uname, country, name, email, link, get_scholar_profile(name)])

def yonsei_uni():
    url = "https://devcms.yonsei.ac.kr/engineering_en/about/major_9_2.do"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    all_profs = soup.find_all('div', class_='board-faculty-box')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Yonsei University done...")
    print()
    return faculty_data

if __name__ == '__main__':
    yonsei_uni()