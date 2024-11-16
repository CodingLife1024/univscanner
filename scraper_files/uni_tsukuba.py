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

u_name = "University of Tsukuba"
country = "Japan"

def get_faculty_data(prof):
    name = prof.find('th').text.strip()
    lastname = prof.find('a').text
    firstname = name.replace(lastname, '').strip()
    name = (firstname + " " + lastname).title().replace("*", "")
    link = prof.find('a').get('href')
    research = prof.find('td').text.strip()
    email = "N/A"

    if link.startswith("https://www.cs.tsukuba.ac.jp/"):
        email_parts = link.split("/")
        email_parts.reverse()
        for i in email_parts:
            if "~" == i[0]:
                email = i[1:] + "@cs.tsukuba.ac.jp"
                break

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_tsukuba():
    url = "https://www.cs.tsukuba.ac.jp/english/faculties.html#1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')

    all_profs = []

    for i in super_class:
        all_profs.extend(i.find_all('tr'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity of Tsukuba done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_tsukuba()