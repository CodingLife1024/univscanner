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

u_name = "Instituto de Computação - UNICAMP"
country = "Brazil"

def get_faculty_data(prof):
    name = prof.find('h4', {'class': 'name'}).find('a').text.strip()
    link = prof.find('h4', {'class': 'name'}).find('a')['href']

    title = prof.find('span', {'class': 'cargo'}).text.strip() if prof.find('span', {'class': 'cargo'}) else "N/A"

    if "professor" in title.lower() or "lecturer" in title.lower():
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('span', class_="label", string="E-mail").find_next('span').text.strip() if new_soup.find('span', class_="label", string="E-mail") else "N/A"

        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def unicamp():
    urls = ["https://www.ic.unicamp.br/en/docentes/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'people-box'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Instiuto de Computação - UNICAMP done...")
    print()
    return faculty_data

if __name__ == '__main__':
    unicamp()