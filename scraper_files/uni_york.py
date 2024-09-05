import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "University of York"
country = "United Kingdom"

def get_faculty_data(prof, headers):
    columns = prof.find_all("td")
    if len(columns) < 2:
        return
    name = columns[1].find("a").get_text().replace("Dr", "").strip() if columns[1].find("a") else None
    link = "https://www.cs.york.ac.uk/people/" + columns[1].find("a")["href"] if columns[1].find("a") else None
    email = prof.find("a", string="E-mail")['href'] if prof.find("a", string="E-mail") else None

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_york():
    url = "https://www.cs.york.ac.uk/people/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
        }

    r = requests.get(url, headers=headers)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find("table", class_="searchbox").find_all("tr")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of York done...")
    print()
    return faculty_data


if __name__ == '__main__':
    uni_york()
