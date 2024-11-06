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

u_name = "Universiti Sains Malaysia"
country = "Malaysia"

def get_faculty_data(prof, headers):
    link = "https://cs.usm.my" + prof.find('a', href=True)['href'] if prof.find('a', href=True) else None
    name = prof.find('a').get_text().strip() if prof.find('a') else None

    if not link or not name:
        return
    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text
    email = "Not Found"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def usm_malaysia():
    url = "https://cs.usm.my/index.php/about/our-people/facultycs-member"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('span', style="font-size: 12pt; font-family: arial, helvetica, sans-serif;")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversiti Sains Malaysia done...\n")
    return faculty_data

if __name__ == '__main__':
    usm_malaysia()