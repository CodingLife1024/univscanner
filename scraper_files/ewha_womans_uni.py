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

u_name = "Ewha Womans University"
country = "South Korea"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    if len(columns) >= 5:
        name = columns[0].find('p').text.strip()
        title = name.split('(')[1].strip().lower()
        name = name.split("(")[0].strip()
        if "emeritus" not in title:
            email = columns[3].text.strip()
            link = columns[4].find('a').get('href')
            research = columns[2].text.strip()

            found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                pers_link = get_scholar_profile(name)
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])

def ewha_womans_uni():
    url = "http://cms.ewha.ac.kr/user/indexSub.action?codyMenuSeq=2172651&siteId=cseeng&menuUIType=sub"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('tbody')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nEwha Womans University done...\n")
    return faculty_data


if __name__ == '__main__':
    ewha_womans_uni()