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

u_name = "Brunel University of London"
country = "United Kingdom"

def get_faculty_data(prof):
    columns = prof.find_all('td')

    name = columns[1].find('a').text.replace("Dr", "").replace("Professor", "").strip()
    link = "https://www.brunel.ac.uk" + columns[1].find('a')['href']
    email = columns[3].text.strip() if columns[3].text.strip() else "N/A"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def brunel_uni():
    urls = [
        "https://www.brunel.ac.uk/people/cedps/computer?filter=academic",
        "https://www.brunel.ac.uk/people/cedps/electronic?filter=academic",
    ]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        profs = soup.find('tbody').find_all('tr')
        all_profs += profs

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nBrunel University of London done...\n")
    return faculty_data


if __name__ == '__main__':
    brunel_uni()