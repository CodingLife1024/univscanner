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
from components.search_expertise import search_expertise

faculty_data = []

u_name = "University of Miami"
country = "United States"

def get_faculty_data_1(prof, headers):
    name = prof.find('a').text.strip()
    link = prof.find('a').get('href').replace(" /", "https:/").strip()
    hex_string = prof.find('div', class_="profile-contact-email").find('a').get('data-code')
    hex_codes = [hex_string[i:i+4] for i in range(0, len(hex_string), 4)]
    email = ''.join([chr(int(code, 16)) for code in hex_codes])

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    pers_link = get_scholar_profile(name)

    research = new_soup.text + search_expertise(pers_link, headers)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof, headers):
    name = prof.find('a').text.strip()
    link = prof.find('a').get('href').replace(" /", "https:/").strip()
    hex_string = prof.find('a', class_="email-decode hide").get('data-code')
    hex_codes = [hex_string[i:i+4] for i in range(0, len(hex_string), 4)]
    email = ''.join([chr(int(code, 16)) for code in hex_codes])

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    pers_link = get_scholar_profile(name)

    research = new_soup.text + search_expertise(pers_link, headers)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_miami():
    urls = [
        "https://csc.as.miami.edu/people/index.html",
        "https://ece.coe.miami.edu/people/faculty/index.html"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }

    # for url 1

    url = urls[0]
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('li', class_="people-profile clearfix")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for url 2
    url = urls[1]
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="profile-content")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Miami done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_miami()