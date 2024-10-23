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

u_name = "University of Surrey"
country = "United Kingdom"

def get_faculty_data(prof):
    name = prof.find('h3').text.replace("Dr", "").replace("Professor", "").strip()
    link = "https://www.surrey.ac.uk/" + prof.find('a').get('href')

    research = prof.text

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research += new_soup.text

    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_surrey():
    url = "https://www.surrey.ac.uk/computer-science-research-centre/people/academic-staff"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'col-12 col-md-6 col-lg-4 mb-gw'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Surrey done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_surrey()