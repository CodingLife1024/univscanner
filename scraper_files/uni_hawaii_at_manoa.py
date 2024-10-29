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

u_name = "University of Hawaiʻi at Mānoa"
country = "United States"

def get_faculty_data(prof):
    name = prof.find('a').text.strip()
    link = prof.find('a').get('href')
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    research = prof.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = prof.find_all('a')[-1].get('href') if prof.find_all('a')[-1].get('href') != link else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_hawaii_at_manoa():
    urls = [
        "https://www.ics.hawaii.edu/people/"
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'wp-block-column is-layout-flow wp-block-column-is-layout-flow', "style": "flex-basis:20%"})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Hawaiʻi at Mānoa done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_hawaii_at_manoa()