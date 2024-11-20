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

u_name = "University of Liverpool"
country = "United Kingdom"

def get_faculty_data(prof, headers):
    columns = prof.find_all('td')

    full_name = columns[0].text.strip().split(",")
    name = full_name[1] + " " + full_name[0]
    name = name.replace("Dr ", "").replace("Prof ", "").replace("Professor ", "").replace("Mr ", "").replace("Ms ", "").replace("Mrs ", "").replace("Miss ", "").replace("Dr. ", "").replace("Prof. ", "").replace("Mr. ", "").replace("Ms. ", "").replace("Mrs. ", "").replace("Miss. ", "")

    email = columns[2].text.strip()

    link = columns[0].find('a')['href']

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_liverpool():
    url = "https://www.liverpool.ac.uk/computer-science/staff/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')[0:2]

    all_profs = []

    for i in super_class:
        profs = i.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Liverpool done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_liverpool()