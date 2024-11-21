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

u_name = "City University of London"
country = "United Kingdom"

def get_faculty_data(prof):
    name = prof.text.replace("Dr", "").replace("Professor", "").strip()
    link = prof.get('href')

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text.strip()

    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def city_uni_london():
    urls = [
        "https://www.city.ac.uk/about/schools/science-technology/computer-science#tabs561080-link580290",
        "https://www.city.ac.uk/about/schools/science-technology/mathematics",
        "https://www.city.ac.uk/about/schools/science-technology/engineering#tabs580800-link580813"
    ]

    all_profs = []

    for url in urls:
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")

        profs = soup.find('ul', class_="paginated-list").find_all('a')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nCity University of London done...\n")

    return faculty_data

if __name__ == '__main__':
    city_uni_london()


