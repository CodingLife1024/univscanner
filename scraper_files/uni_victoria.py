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

u_name = "University of Victoria"
country = "Canada"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].find('a').text.strip() if columns[0].find('a') else columns[0].text.strip()
    link = "https://www.uvic.ca/ecs/computerscience/people/faculty/" + columns[0].find('a').get('href')
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    research = columns[1].text

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research += new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = prof.find('a', string="website").get('href') if prof.find('a', string="website") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_victoria():
    url = "https://www.uvic.ca/ecs/computerscience/people/faculty/index.php"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Victoria done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_victoria()