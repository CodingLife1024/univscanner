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

u_name = "Norwegian University of Science and Technology"
country = "Norway"

def get_faculty_data(prof):
    name = prof.find('strong', class_='fullname').text[:-1].strip()
    link = "https://www.ntnu.edu" + prof['href']
    title = prof.find('span', class_='role').text.strip().lower()

    if ("professor" in title or "lecturer" in title) and "emerit" not in title:
        email = prof.find('span', class_='email').text.strip()

        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research = new_soup.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def norwegian_uni():
    url = "https://www.ntnu.edu/idi/people/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('a', class_='contactDetails')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNorwegian University of Science and Technology done...\n")
    return faculty_data

if __name__ == '__main__':
    norwegian_uni()
