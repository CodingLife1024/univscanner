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

u_name = "North Carolina State University"
country = "United States"

def get_name(prof):
    name_string = prof.find('a').text.replace("Dr.", "").replace("Ms.", "").replace("Mr.", "").strip()
    name_parts = name_string.split(" ")
    name_parts = [part for part in name_parts if part != ""]
    name = " ".join(name_parts)
    return name

def get_email(prof):
    email = prof.find_all('h6')[-1].text.strip() if prof.find_all('h6') else "N/A"
    return email

def get_link(prof):
    link = "https://www.csc.ncsu.edu/" + prof.find('a').get('href')
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

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = new_soup.find('a', string="Web Site")['href'] if new_soup.find('a', string="Web Site") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def north_carolina_state_uni():
    urls = [
        "https://www.csc.ncsu.edu/directories/faculty.php",
        "https://www.csc.ncsu.edu/directories/adjunct.php"
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'person'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNorth Carolina State University done...\n")
    return faculty_data


if __name__ == '__main__':
    north_carolina_state_uni()