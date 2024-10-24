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

u_name = "Dalhousie University"
country = "Canada"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    if len(columns) >= 2:
        name = columns[0].find('a').text.replace("Dr.", "").replace("\xa0", " ").replace("Mr.", "").strip()
        email = columns[1].text.strip()
        link = "https://www.dal.ca" + columns[0].find('a').get('href') if columns[0].find('a') else "N/A"

        if link != "N/A":
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            research = new_soup.text

            found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                pers_link = get_scholar_profile(name)
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])


def dalhousie_uni():
    url = "https://www.dal.ca/faculty/computerscience/faculty-staff.html"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    super_class = soup.find_all('tbody')

    super_table = super_class[1:6]

    all_profs = []

    for table in super_table:
        profs = table.find_all('tr')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nDalhousie University done...\n")
    return faculty_data


if __name__ == '__main__':
    dalhousie_uni()