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

u_name = "Curtin University"
country = "Australia"

def get_faculty_data(prof, headers):
    columns = prof.find_all('td')
    name = columns[0].text.replace("Mr", "").replace("Dr", "").replace("Professor", "").replace("Associate", "").replace("Ms", "").strip() if columns[0].text else "N/A"
    position = columns[1].text.strip().lower()
    link = columns[0].find('a')['href'] if columns[0].find('a') else "N/A"

    if "professor" in position or "lecturer" in position:
        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('a', href=re.compile(r'mailto:'))['href'].split(":")[1] if new_soup.find('a', href=re.compile(r'mailto:')) else "N/A"

        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = "get_scholar_profile(name)"
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def curtin_uni():
    urls = ["https://www.curtin.edu.au/about/learning-teaching/science-engineering/school-of-electrical-engineering-computing-and-mathematical-sciences/our-people/"]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    super_class = soup.find_all('tbody')

    all_profs = []

    for s in super_class:
        profs = s.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nCurtin University done...\n")
    return faculty_data


if __name__ == "__main__":
    curtin_uni()