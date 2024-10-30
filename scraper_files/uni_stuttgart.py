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

u_name = "University of Stuttgart"
country = "Germany"

def get_faculty_data(prof):
    name = prof.find('a').text.strip().split(".")[-1]
    link = prof.find('a').get('href')
    email = name.split(" ")[0].lower() + "@" + name.split(" ")[1].lower() + "informatik.uni-stuttgart.de"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_stuttgart():
    urls = [
        "https://www.iti.uni-stuttgart.de/en/institute/team/",
        "https://www.f05.uni-stuttgart.de/en/cs/department/professors/",
        "https://www.f05.uni-stuttgart.de/en/ei/department/professors"
    ]

    all_profs = []

    url = urls[0]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    super_class = soup.find_all("div", class_="row flex-row generic-list")[:1]
    for i in super_class:
        curr_profs = i.find_all('div', {'class': 'text'})
        all_profs.extend(curr_profs)

    url = urls[1]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    super_class = soup.find_all("div", class_="row flex-row generic-list")[:-1]
    for i in super_class:
        curr_profs = i.find_all('div', {'class': 'text'})
        all_profs.extend(curr_profs)

    url = urls[2]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    super_class = soup.find_all("div", class_="row flex-row generic-list")[:1]
    for i in super_class:
        curr_profs = i.find_all('div', {'class': 'text'})
        all_profs.extend(curr_profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity of Stuttgart done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_stuttgart()