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

u_name = "National Yang Ming Chiao Tung University"
country = "Taiwan"

def get_faculty_data(prof):
    name = prof.find('h2').find('small').text.strip()
    link = prof.find('a').get('href')

    new_r = requests.get(link, verify=True)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text
    email = new_soup.find('i', class_="fa fa-envelope-o").find_next('span').text.replace("[at]", "@") if new_soup.find('i', class_="fa fa-envelope-o") else "N/A"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('i', class_="fa fa-home").find_next('a').get('href') if new_soup.find('i', class_="fa fa-home") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def national_yang_ming_chiao_tung_uni():
    urls = ["https://www.cs.nycu.edu.tw/members/prof"]

    total_text = ""

    for url in urls:
        r = requests.get(url, verify=True)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'card member-card'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNational Yang Ming Chiao Tung University done...\n")
    return faculty_data

if __name__ == '__main__':
    national_yang_ming_chiao_tung_uni()