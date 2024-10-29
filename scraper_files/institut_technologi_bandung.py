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

u_name = "Institut Teknologi Bandung"
country = "Indonesia"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip()
    link = columns[0].find('a')['href']

    email = "N/A"

    new_r = requests.get(link, verify=False)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def institut_technologi_bandung():
    urls = ["https://itb.ac.id/staff/listby"]

    total_text = ""

    for url in urls:
        r = requests.get(url, verify=False)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nInstiut Teknologi Bandung done...\n")
    return faculty_data

if __name__ == "__main__":
    institut_technologi_bandung()