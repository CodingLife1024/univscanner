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

u_name = "National Taiwan University of Science and Technology"
country = "Taiwan"

def get_faculty_data(prof):
    name = prof.find('div', class_="mtitle").text.replace("\n", "").replace("\t", "").replace("Professor", "").replace("Associate", "").replace("Assistant", "").replace("Project", "").replace("Chairman", "").replace(",", "").replace("Distinguished", "").replace("Chair", "").strip()
    link = prof.find('div', class_="mtitle").find('a')['href']
    table = prof.find('tbody').find_all('td')
    email = table[1].text.strip()
    pers_link = table[3].text.strip()

    research = prof.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def national_taiwan_uni():
    urls = ["https://csie-r.ntust.edu.tw/p/412-1038-1815.php?Lang=en"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="d-item h-il-td col-sm-12")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNational Taiwan University of Science and Technology done...")
    return faculty_data


if __name__ == "__main__":
    national_taiwan_uni()