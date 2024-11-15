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

u_name = "University of Nottingham"
country = "United Kingdom"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name_parts = columns[0].text.strip().split(",")
    name = name_parts[1].strip() + " " + name_parts[0].strip()
    link = "https://www.nottingham.ac.uk/computerscience/people/" + columns[0].find('a')['href']
    email = prof.find('a', href=re.compile(r'^mailto:'))['href'][7:] if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

    new_r = requests.get(link)
    research = new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_nottingham():
    url = "https://www.nottingham.ac.uk/computerscience/people/index.aspx"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('tr')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Nottingham done...\n")
    return faculty_data

if __name__ == "__main__":
    uni_nottingham()