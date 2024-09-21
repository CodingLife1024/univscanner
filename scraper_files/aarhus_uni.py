import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Aarhus University"
country = "Denmark"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].get_text().split(",")[1].strip() + " " + columns[0].get_text().split(",")[0].strip()
    link = "https://cs.au.dk" + columns[0].find('a')['href']
    title = columns[1].get_text().strip()
    email = columns[2].get_text().strip()

    if "professor" in title.lower() or "lecturer" in title.lower():
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text
        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def aarhus_uni():
    urls = ["https://cs.au.dk/contact/people/",
            "https://cs.au.dk/contact/people?tx_pure_pure5%5Bcontroller%5D=Persons&tx_pure_pure5%5Bpointer%5D=1&cHash=0639fec7f44f19e6a3366d80c67af9fc"]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        subclass = soup.find('table', class_="pure-persons-table").find_all('tr')[1:]
        all_profs.extend(subclass)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Aarhus University done...")
    print()

    return faculty_data

if __name__ == '__main__':
    aarhus_uni()
