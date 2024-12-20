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

u_name = "University of Leicester"
country = "United Kingdom"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].text.replace("Dr", "").strip()
    position = columns[1].text.strip()
    link = columns[0].find('a').get('href') if columns[0].find('a') else "N/A"
    email = columns[3].text.strip()

    if link != "N/A" and link[0] == "/":
        link = "https://le.ac.uk" + link

    if link != "N/A" and (position == "Academic" or position == "Head of School" or position == "Deputy Head"):
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_leicester():
    urls = ["https://le.ac.uk/computing-and-mathematical-sciences/people/academic"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Leicester done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_leicester()