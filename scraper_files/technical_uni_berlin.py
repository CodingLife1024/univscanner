import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import base64
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name= "Technische Universität Berlin"
country = "Germany"

def get_faculty_data(prof):
    columns = prof.find_all("td")
    name = columns[0].get_text().strip()
    link = columns[0].find("a")["href"] if columns[0].find("a") else None

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = name.split(",")[1].lower() + "." + name.split(",")[0].lower() + "@tu-berlin.de"
    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def technical_uni_berlin():
    url = "https://www.tu.berlin/en/eecs/institutions/professors-chairs"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find("div", class_="frame frame--type-table")

    all_profs = super_class.find_all("tr")[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Technische Universität Berlin done...")
    print()
    return faculty_data


if __name__ == '__main__':
    technical_uni_berlin()