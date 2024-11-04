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

university = "Tsinghua University"
country = "China"

def get_faculty_data(prof):
    name = prof.find('a').text
    site = "https://www.cs.tsinghua.edu.cn/csen" + prof.find('a')['href'][2:]
    email = prof.find_all('p')[2].text

    new_r = requests.get(site)
    found_keyword = any(re.search(re.escape(keyword), new_r.text) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        print([university, country, name, email, site, pers_link])
        faculty_data.append([university, country, name, email, site, pers_link])

def tsinghua():
    url = "https://www.cs.tsinghua.edu.cn/csen/Faculty/Full_time_Faculty.htm"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('div', class_='text')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTsinghua University done...\n")
    return faculty_data


if __name__ == '__main__':
    tsinghua()
    