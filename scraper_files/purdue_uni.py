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

u_name = "Purdue University"
country = "United States"

def get_faculty_data_1(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip() if len(columns) > 0 else None
    email = None
    if len(columns) > 4 and columns[4].find('a'):
        email = columns[4].find('a')['href'].replace('mailto:', '')
    link = None
    if len(columns) > 5 and columns[5].find('a'):
        link = "https://www.cs.purdue.edu/people/faculty/" + columns[5].find('a')['href']

    if link is not None:
        new_r = requests.get(link)
        research = new_r.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof):
    name = prof.find('a').text.strip()
    link = prof.find('a')['href']
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"

    new_r = requests.get(link)
    research = new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def purdue_uni():
    urls = ["https://www.cs.purdue.edu/people/faculty/index.html",
            "https://engineering.purdue.edu/ECE/People/Faculty"]

    # url 1
    r = requests.get(urls[0])
    soup = BeautifulSoup(r.text, 'html.parser')

    table_professor = soup.find('table', class_='directory table table-bordered table-striped table-condensed')

    all_profs = table_professor.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    # url 2
    r = requests.get(urls[1])

    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('div', class_='col-8 col-sm-9 list-info')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Purdue University done...")
    print()
    return faculty_data


if __name__ == "__main__":
    purdue_uni()