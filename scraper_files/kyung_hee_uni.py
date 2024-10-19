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

u_name = "Kyung Hee University"
country = "South Korea"

def get_faculty_data(prof):
    name = prof.find('h3').text.strip()
    link = prof.find('a').get('href')
    email = prof.find('a', {'data-md5': True}).text.strip() if prof.find('a', {'data-md5': True}) else "N/A"
    pers_link = get_scholar_profile(name)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def kyung_hee_uni():
    urls = ["https://khu.elsevierpure.com/en/organisations/computer-science-and-engineering/persons/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'result-container'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Kyung Hee University done...")
    print()
    return faculty_data

if __name__ == "__main__":
    kyung_hee_uni()