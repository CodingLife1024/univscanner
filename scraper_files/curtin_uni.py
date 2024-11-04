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

def get_faculty_data(prof):
    try:
        name_elem = prof.find('a')
        name = name_elem.text.replace('Dr', "").strip() if name_elem else "N/A"
        link = name_elem['href'] if name_elem else "N/A"

        td_elements = prof.find_all('td')
        title = td_elements[-1].text.strip().lower() if td_elements else "N/A"

        if "professor" in title or "lecturer" in title:
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            email_elem = new_soup.find('a', href=re.compile(r'^mailto:'))
            email = email_elem['href'].split(':')[1] if email_elem else "N/A"

            research = new_soup.get_text()
            found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                pers_link = get_scholar_profile(name)
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])

    except Exception as e:
        print(f"Error occurred: {e}")


def curtin_uni():
    urls = ["https://www.curtin.edu.au/about/learning-teaching/science-engineering/school-of-electrical-engineering-computing-and-mathematical-sciences/our-people/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nCurtin University done...\n")
    return faculty_data


if __name__ == "__main__":
    curtin_uni()