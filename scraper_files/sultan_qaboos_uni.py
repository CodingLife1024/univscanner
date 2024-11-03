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

u_name = "Sultan Qaboos University"
country = "Oman"

def get_faculty_data(prof):
    name = prof.find('h2').text.strip()
    link = prof.find('a').get('href')
    research = prof.text
    email = research.split("Email:")[-1].split("@")[0].replace("\xa0", "") + "@squ.edu.om"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def sultan_qaboos_uni():
    url = "https://www.squ.edu.om/science/Departments/Computer-Science/Department-People/Faculty"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('tr', class_="dnnGridItem")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSultan Qaboos University done...\n")
    return faculty_data


if __name__ == "__main__":
    sultan_qaboos_uni()