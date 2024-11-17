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

u_name = "Southern University of Science and Technology"
country = "China"

def get_faculty_data_1(prof):
    link = "https://math.sustech.edu.cn" + prof.find('a').get('href')
    name = prof.find('li', class_="name").text.title()
    research = prof.text

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('span', class_="email fl").text.strip() if new_soup.find('span', class_="email fl") else "N/A"

    research += new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    link = "https://siqse.sustech.edu.cn" + prof.find('a').get('href')
    name = prof.find('h4', class_="title").text.title().split("\\")[0].strip()
    research = prof.text

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = "N/A"

    research += new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def sustech():
    urls = [
        "https://math.sustech.edu.cn/user/all/1.html?lang=en",
        "https://siqse.sustech.edu.cn/Index/staff/mid/58"
    ]

    # for url 1

    r = requests.get(urls[0], verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = []

    super_class = soup.find_all('div', class_="thumb-wrap clearfix")

    for i in super_class:
        all_profs += i.find_all('div', class_="item fl")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 2

    r = requests.get(urls[1], verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="col-xs-12 col-md-6")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSouthern University of Science and Technology done...\n")
    return faculty_data


if __name__ == '__main__':
    sustech()