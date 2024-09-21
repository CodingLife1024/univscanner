import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Aalto University"
country = "Finland"

def get_name(prof):
    return prof.text.strip()

def get_link(prof):
    return prof['href']

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link)
    research = new_r.text

    email = "N/A"
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def aalto_uni():
    url = "https://research.aalto.fi/en/organisations/computer-science-professors/persons/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('a', class_="link person")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Aalto University done...")
    print()

    return faculty_data


if __name__ == '__main__':
    aalto_uni()