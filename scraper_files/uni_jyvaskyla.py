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

u_name = "University of Jyväskylä"
country = "Finland"

def get_faculty_data(prof, headers):
    link = "https://www.jyu.fi" + prof.get('href')
    name = prof.find('h3').text.strip()
    title = prof.find('div', class_="field field--name-field-person-title field--label-hidden").text.strip().lower()

    if "professor" or "lecturer" in title:
        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research = new_soup.text

        email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_jyvaskyla():
    urls = [
        "https://www.jyu.fi/fi/it/yhteystiedot",
        "https://www.jyu.fi/fi/it/yhteystiedot?page=1",
        "https://www.jyu.fi/fi/it/yhteystiedot?page=2",
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Accept-Language': 'en'
    }

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('a', {'class': 'liftup liftup--person liftup--minimal'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Jyväskylä done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_jyvaskyla()