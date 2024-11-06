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

u_name = "University of Copenhagen"
country = "Denmark"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip()
    link = "https://di.ku.dk/english/staff/vip/" + columns[0].find('a').get('href')
    post = columns[1].text.strip().lower()

    if "professor" in post or "lecturer" in post:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('p', class_="forskerprofil_kontakt").find('a').text.strip() if new_soup.find('p', class_="forskerprofil_kontakt").find('a') else "N/A"
        research = new_soup.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_copenhagen():
    url = "https://di.ku.dk/english/staff/vip/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    tbody = soup.find('tbody')
    all_profs = tbody.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Copenhagen done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_copenhagen()