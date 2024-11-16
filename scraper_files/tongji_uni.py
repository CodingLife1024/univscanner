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

u_name = "Tongji University"
country = "China"

def get_faculty_data(prof):
    name = prof.find('a')['title']
    link = "https://see-en.tongji.edu.cn" + prof.find('a').get('href')[2:]

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text
    email = new_soup.find('strong', string="Email:").find_parent('p').text.split(":")[-1].strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('strong', string="Personal home page:").find_parent('p').text.split(":")[-1].strip() if new_soup.find('strong', string="Personal home page:") else get_scholar_profile(name)
        if pers_link == "":
            pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def tongji_uni():
    urls = [
        "https://see-en.tongji.edu.cn/faculty/By_A_Z.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/11.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/10.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/9.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/8.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/7.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/6.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/5.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/4.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/3.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/2.htm",
        "https://see-en.tongji.edu.cn/faculty/By_A_Z/1.htm"
        ]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        print("Scraping: ", url)
        soup = BeautifulSoup(r.text, "html.parser")
        super_container = soup.find_all('ul')[-1].find_all('li')
        all_profs.extend(super_container)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTongji University done...\n")
    return faculty_data


if __name__ == '__main__':
    tongji_uni()