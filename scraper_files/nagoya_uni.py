import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "Nagoya University"
country = "Japan"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip() if len(columns) > 0 else None
    if name is not None:
        name = name.split(',')[1].capitalize() + " " + name.split(',')[0].capitalize()
    else:
        pass
    email = columns[3].text.strip() + "@i.nagoya-u.ac.jp" if len(columns) > 3 else None
    link = columns[5].find('a')['href'] if len(columns) > 5 and columns[5].find('a') else None
    pers_link = columns[7].find('a')['href'] if len(columns) > 7 and columns[7].find('a') else get_scholar_profile(name)

    research = columns[4].text.strip() if len(columns) > 4 else ""

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def nagoya_uni():
    urls = ["https://www.i.nagoya-u.ac.jp/en/prof/study_a06/",
            "https://www.i.nagoya-u.ac.jp/en/prof/study_a09/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, 'html.parser')

    all_profs = soup.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Nagoya University done...")
    print()

    return faculty_data

if __name__ == "__main__":
    nagoya_uni()