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

u_name = "Humboltd University of Berlin"
country = "Germany"

faculty_data = []

def get_faculty_data(prof):
    name = prof.find('a').text.strip().split(",")[1].strip() + " " + prof.find('a').text.strip().split(",")[0].strip()
    link = prof.find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    email = new_soup.find('dt', string='E-Mail').find_next('dd').text.strip().replace(' (at) ', '@')
    research = new_r.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_berlin():
    url = "https://www.informatik.hu-berlin.de/de/org/mitarbeiter"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('dd', class_='view_content')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nHumoltd University of Berlin done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_berlin()