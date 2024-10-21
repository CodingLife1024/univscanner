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

u_name = "Universitas Gadjah Mada"
country = "Indonesia"

def get_faculty_data_1(prof):
    columns = prof.find_all('td')
    name = columns[1].text.strip().split(',')[0]
    link = columns[1].find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    email = new_soup.find('td').text[8:].strip() if new_soup.find('td') else "N/A"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword or True:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip().split(',')[0]
    link = columns[0].find('a')['href']
    email = "N/A"

    pers_link = get_scholar_profile(name)
    faculty_data.append([u_name, country, name, email, link, pers_link])
    print([u_name, country, name, email, link, pers_link])

def universitas_gadjah_mada():
    urls = ["https://dcse.fmipa.ugm.ac.id/?page_id=270&lang=en",
            "https://dcse.fmipa.ugm.ac.id/?page_id=1072&lang=en",
            "https://dcse.fmipa.ugm.ac.id/?page_id=1069&lang=en"]

    # url 1
    r = requests.get(urls[0])

    soup = BeautifulSoup(r.text, "html.parser")
    all_profs = soup.find('tbody').find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # url 2
    r = requests.get(urls[1])

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # url 3
    r = requests.get(urls[2])

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('tbody').find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversitas Gadja Mada done...\n")
    return faculty_data


if __name__ == '__main__':
    universitas_gadjah_mada()