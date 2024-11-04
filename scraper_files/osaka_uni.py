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

u_name = "Osaka University"
country = "Japan"

def get_email(new_soup):
    email_tag = new_soup.find('div', class_="researcherDetailContact").find_all('p')[1].text[7:]
    email = email_tag + "osaka-u.ac.jp" if email_tag else "N/A"
    return email

def get_faculty_data(prof):
    link = "https://www.ist.osaka-u.ac.jp/english/researcher" + prof['href'][1:]
    name = prof.find('p', class_="researcherListBoxStr2").text.strip()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    new_soup.find('div', class_='researcherDetailMainBox2').text.strip()

    found_keyword = any(re.search(re.escape(keyword), new_soup.text, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword or True:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_email = executor.submit(get_email, new_soup)
            pers_link = executor.submit(get_scholar_profile, name)
            email = future_email.result()
            pers_link = pers_link.result()
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def osaka_uni():
    url = "https://www.ist.osaka-u.ac.jp/english/researcher/list.php?id=3"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_proffs = soup.find_all('a', class_='researcherListBox')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_proffs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Ensure exceptions are raised
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nOsaka University done...\n")
    return faculty_data

if __name__ == '__main__':
    osaka_uni()

