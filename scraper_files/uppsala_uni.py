import requests
import sys
import os
import re
import concurrent.futures

from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

u_name = "Uppsala University"
country = "Japan"

faculty_data = []

def get_name(prof):
    name = prof.find('span').find('a').text.strip()
    return name

def get_link(prof):
    link = "https://www.uu.se" + prof.find('span').find('a')['href']
    return link

def get_title(prof):
    title = prof.find('ul').find('li').text.strip()
    return title

def get_email(prof):
    email = prof.find('a', class_='email').text.strip() if prof.find('a', class_='email') else None
    return email

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_title = executor.submit(get_title, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        title = future_title.result()

    if (("professor" in title.lower() or "lecturer" in title.lower()) and "emeritus" not in title.lower()) and email:
        new_r = requests.get(link, headers=headers)
        research = new_r.text
        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uppsala_uni():
    url = "https://www.uu.se/en/contact-and-organisation/organisation?query=X61%3A1"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='search-result-hit-text-container')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Uppsala University done...")
    print()
    return faculty_data

if __name__ == '__main__':
    uppsala_uni()
