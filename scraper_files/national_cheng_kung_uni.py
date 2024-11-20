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

u_name = "National Cheng Kung University"
country = "Taiwan"

def get_faculty_data_1(prof):
    name = prof.find('div', class_="avatar__name").text.strip()
    link = prof.find('a').get('href')
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    pers_link = prof.find("div", class_="avatar-info__item").find('a')['href'] if prof.find("div", class_="avatar-info__item").find('a') else "get_scholar_profile(name)"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    name = prof.find('h3').text.strip()
    link = prof.find('a').get('href')
    email = prof.find('a', {'data-md5': True}).text.strip() if prof.find('a', {'data-md5': True}) else "N/A"
    pers_link = get_scholar_profile(name)

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def national_cheng_kung_uni():
    urls = ["https://computing.ncku.edu.tw/en/member/professor",
            "https://researchoutput.ncku.edu.tw/en/organisations/department-of-computer-science-and-information-engineering/persons/"]

    # for 1st url

    url = urls[0]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'avatar-item'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # for 2nd url
    url = urls[1]

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'result-container'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNational Cheng Kung University done...\n")
    return faculty_data


if __name__ == '__main__':
    national_cheng_kung_uni()