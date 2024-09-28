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

u_name = "Technical University of Vienna"
country = "Austria"

def get_faculty_data(prof):
    link = 'https://informatics.tuwien.ac.at' + prof.find('a')['href']
    link_name = prof.find('a').text.strip()
    title = prof.find('div', class_='text-truncate text-muted').text.strip()
    name = prof.find('p').text.strip()
    name = link_name + " " + name.replace(link_name, '').replace(title, '').replace(',', " ").strip()

    if ("professor" in title or "lecturer" in title) and "emerit" not in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip()
        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = new_soup.find('ul', class_="mt-4").find_all('a')[-1] if new_soup.find('ul', class_="mt-4") else get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def tu_wien():
    url = "https://informatics.tuwien.ac.at/people/all"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='col-12 col-sm-6 col-md-4 col-lg-3')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Technical University of Vienna done...")
    print()
    return faculty_data


if __name__ == '__main__':
    tu_wien()

