import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "University of Tübingen"
country = "Germany"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    if len(columns) < 4:
        return
    name_parts = columns[0].get_text().strip().split(',')
    name = name_parts[1].strip() + " " + name_parts[0].strip()
    link = "https://www.embedded.uni-tuebingen.de" + columns[0].find('a')['href']
    email = columns[3].find('a')['href'][7:] if columns[3].find('a') else "N/A"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_tubingen():
    url = "https://www.embedded.uni-tuebingen.de/en/team/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('table').find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Tübingen done...")
    print()

    return faculty_data


if __name__ == "__main__":
    uni_tubingen()