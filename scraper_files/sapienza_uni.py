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

u_name = "Sapienza University di Roma"
country = "Italy"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].find('a').get_text().strip()
    link = "https://www.di.uniroma1.it" + columns[0].find('a')['href']
    email = columns[2].get_text().strip()
    email = email.replace(".", "@")

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)

        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def sapienza_uni():
    url = "https://www.di.uniroma1.it/en/people/professors"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('tr', {'class':["odd", 'even']})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSapienza University di Roma done...\n")
    return faculty_data

if __name__ == '__main__':
    sapienza_uni()