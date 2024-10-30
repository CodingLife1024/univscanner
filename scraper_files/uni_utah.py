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

u_name = "University of Utah"
country = "United States"

def get_faculty_data_1(prof, headers):
    if prof.find('a'):
        name = prof.find('h2').text.strip()
        link = prof.find('a')['href']
        email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

        pers_link = prof.find('a', string="Website")['href'] if prof.find('a', string="Website") else get_scholar_profile(name)
        research = prof.text.strip()

        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research += new_soup.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof, headers):
    if prof.find('a', href=lambda x: x.startswith("https://")):
        name = prof.find('h3').text.strip()
        link = prof.find('a')['href']
        email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

        pers_link = prof.find('a', string="Website")['href'] if prof.find('a', string="Website") else get_scholar_profile(name)
        research = prof.text.strip()

        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research += new_soup.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_utah():
    urls = [
        "https://www.cs.utah.edu/people/faculty/",
        "https://www.ece.utah.edu/faculty/"
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

    # for url 1

    url = urls[0]
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="t-inside")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    all_profs = []

    # for url 2

    url = urls[1]
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="t-inside")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Utah done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_utah()

