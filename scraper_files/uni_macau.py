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

u_name = "University of Macau"
country = "Macau SAR"

def get_faculty_data(prof):
    if prof.find('a'):
        name = prof.find('a').text.strip().split(",")[0].title()
        link = prof.find('a')['href']
        research = prof.text
        email = email = research.split('Email: ')[1].split()[0] + "@um.edu.mo" if research else "N/A"

        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research += new_soup.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def uni_macau():
    url = "https://www.cis.um.edu.mo/acadstaff.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Macau done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_macau()