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

u_name = "University of Bergen"
country = "Norway"

def get_faculty_data(prof):
    name = prof.find('div', class_="uib-user-teaser").find('a').get_text().strip()
    link = "https://www.uib.no" + prof.find('div', class_="uib-user-teaser").find('a').get('href')
    email = prof.find('a', href=re.compile(r"^mailto:")).text.strip()
    title = prof.find('p', class_='uib-user-position').text.strip()

    if ("professor" in title.lower() or "lecturer" in title.lower()) and "emerit" not in title.lower():
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def uni_bergen():
    urls = ["https://www.uib.no/en/ii/persons",
            "https://www.uib.no/en/ii/persons?page=1",
            "https://www.uib.no/en/ii/persons?page=2"]

    total_text = ""

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('span', {'class':'field-content'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Bergen done...")
    print()
    return faculty_data

if __name__ == '__main__':
    uni_bergen()