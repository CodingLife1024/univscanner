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

u_name = "Gwangju Institute of Science and Technology (GIST)"
country = "South Korea"

def get_faculty_data_1(prof):
    link = "https://eecs.gist.ac.kr/" + prof.get('href')[1:]
    name = prof.find('div', class_="name").text.replace("\t", "").replace("GIST Distinguished Professor", "").strip()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('div', class_="email").text.strip() if new_soup.find('div', class_="email") else "N/A"
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    link = prof.find('a', string="Homepage").get('href') if prof.find('a', string="Homepage") else "N/A"
    name = prof.find('div', class_="name").text.strip()
    email = prof.find('div', class_="email").text.strip() if prof.find('div', class_="email") else "N/A"

    if link != "N/A":
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def gwangju_uni():
    urls = [
        "https://eecs.gist.ac.kr/m31.php?cate=001001", # 1
        "https://eecs.gist.ac.kr/m31.php?cate=001002&#pageTop", # 2
        "https://eecs.gist.ac.kr/m31.php?cate=001003&#pageTop", #3
        "https://eecs.gist.ac.kr/m31.php?cate=001004&#pageTop", # 2
    ]

    # for url 1

    r = requests.get(urls[0])
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('a', {'class': 'con'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 2, 3, 4

    total_text = ""

    r = requests.get(urls[1])
    total_text += r.text
    r = requests.get(urls[2])
    total_text += r.text
    r = requests.get(urls[3])
    total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('a', {'class': 'con'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nGwangju Institute of Science and Technology (GIST) done...\n")
    return faculty_data


if __name__ == '__main__':
    gwangju_uni()