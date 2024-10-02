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

u_name = "University of Reading"
country = "Malaysia"

def get_faculty_data(prof):
    cols = prof.find_all('td')
    name = cols[0].get_text().replace("Dr", "").replace("Professor", "").replace("Dr.", "").replace("Professor.", "").strip()
    link = cols[0].find('a').get('href')
    if link[0] == '/':
        link = "https://www.reading.ac.uk" + link
    title = cols[1].get_text().strip()
    email = cols[3].get_text().strip()

    if ("professor" or "lecturer" or "head" in title.lower()) and ("emerit" not in title.lower()):

        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_reading():
    urls = ["https://www.reading.ac.uk/computer-science/staff"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    super_class = soup.find_all('tbody')

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')[1:]
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Reading done...")
    print()
    return faculty_data

if __name__ == '__main__':
    uni_reading()
