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

u_name = "University of Aberdeen"
country = "United Kingdom"

def get_faculty_data(prof):
    name = prof.find('td').get_text().replace("Dr", "").replace("Prof", "").replace("Dr.", "").replace("Prof.", "").strip()
    name_parts = name.split(",")
    if len(name_parts) > 1:
        name = name_parts[1] + " " + name_parts[0]
    link = prof.find('a').get('href')
    if link[0] == '/':
        link = "https://www.abdn.ac.uk" + link
    email = prof.find_all('td')[2].find('a')['href'].replace("mailto:", "")

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_aberdeen():
    urls = ["https://www.abdn.ac.uk/ncs/departments/computing-science/people-158.php"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('dd', {'id':"panel1312"}).find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Aberdeen done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_aberdeen()