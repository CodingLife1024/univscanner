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

u_name = "Tokyo University of Technology"
country = "Japan"

def get_faculty_data(prof):
    a = prof.find('a')
    if a == None:
        return
    name = (a.get_text()).strip()
    link = a.get('href')
    cells = prof.find_all('td')
    email = cells[3].text.strip() + "titech.ac.jp" if len(cells) > 3 else "Not Found"

    if link:
        new_r = requests.get(link)
        research_text = new_r.text

        new_soup = BeautifulSoup(research_text, "html.parser")

        found_keyword = any(re.search(re.escape(keyword), research_text.lower()) for keyword in keyword_list)

        if found_keyword:
            pers_page = new_soup.find('a', string='Personal page') if research_text else get_scholar_profile(name.lower())

            print([u_name, country, name, email, link, pers_page])
            faculty_data.append([u_name, country, name, email, link, pers_page])

def tokyo_uni_tech():
    url = "http://www.cs.titech.ac.jp/people-e.html"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('div', {'class':'section'}).find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTokyo University of Technology done...\n")
    return faculty_data


if __name__ == "__main__":
    tokyo_uni_tech()