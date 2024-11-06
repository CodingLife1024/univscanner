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

u_name = "Universitat Munster"
country = "Germany"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name_string = columns[0].text.strip()
    name_pieces = name_string.split(",")
    name = name_pieces[1].strip() + " " + name_pieces[0].strip()
    link = columns[0].find('a')['href']
    title = columns[1].text.strip().lower()
    email = columns[4].text.strip().replace(" dot ", ".").replace(" at ", "@")

    if "dr" in title or "prof" in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research = new_soup.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_munster():
    urls = [
        "https://www.uni-muenster.de/FB10/Service/listinst.shtml#top",
    ]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('table').find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversitat Munster done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_munster()
