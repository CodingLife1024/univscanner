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

u_name = "Simon Fraser University"
country = "Canada"

def get_faculty_data(prof):
    name_parts = prof.find('a').text.split(",")
    name = name_parts[1].strip() + " " + name_parts[0].strip()
    link = "https://www.sfu.ca" + prof.find('a').get('href')
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'][7:] if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    pers_link = new_soup.find('a', class_="faculty-profile-icon personal-site")['href'] if new_soup.find('a', class_="faculty-profile-icon personal-site") else get_scholar_profile(name)

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def simon_fraser_uni():
    urls = [
        "https://www.sfu.ca/fas/computing/people/faculty.html"
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_='clf-fdi__profile')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSimon Fraser University done...\n")
    return faculty_data


if __name__ == '__main__':
    simon_fraser_uni()