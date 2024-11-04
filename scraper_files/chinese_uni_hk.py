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

university = "Chinese University of Hong Kong"
country = "Hong Kong"

def get_faculty_data(prof):
    name = prof.find('div', class_="sptp-member-name").text.strip()
    link = "https://www.cse.cuhk.edu.hk" + prof.find('a')['href'] if prof.find('a') else "N/A"

    if link != "N/A":
        new_r = requests.get(link, verify=False)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        email = new_soup.find('i', class_="fas fa-envelope").find_next('span').text.replace("[at]", "@").replace("[@]", "@")
        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([university, country, name, email, link, pers_link])
            print([university, country, name, email, link, pers_link])

def chinese_uni_hk():
    url = "https://www.cse.cuhk.edu.hk/research/computer-engineering/"

    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'}

    r = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='sptp-member border-bg-around-member sptp-square')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nChinese University of Hong Kong done...\n")
    return faculty_data

if __name__ == '__main__':
    chinese_uni_hk()