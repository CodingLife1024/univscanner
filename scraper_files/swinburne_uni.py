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

u_name = "Swinburne University of Technology"
country = "Australia"

def get_faculty_data(prof):
    columns = prof.find_all('td')

    if len(columns) > 2:
        name = columns[0].text.replace("Dr", "").replace("Professor", "").strip() if columns[0] else "N/A"
        link = columns[0].find('a')['href'] if columns[0].find('a') else "N/A"
        email = columns[2].find('a', href=re.compile(r'^mailto:'))['href'][7:] if columns[2].find('a', href=re.compile(r'^mailto:')) else "N/A"
        title = columns[1].text.strip().lower() if columns[1] else "N/A"

        if "professor" in title or "lecturer" in title:
            if link != "N/A":
                new_r = requests.get(link)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                research = new_soup.text

                found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

                if found_keyword:
                    pers_link = get_scholar_profile(name)
                    faculty_data.append([u_name, country, name, email, link, pers_link])
                    print([u_name, country, name, email, link, pers_link])

def swinburne_uni():
    urls = [
        "https://www.swinburne.edu.au/about/our-structure/organisational-structure/schools-departments/school-science-computing-engineering-technologies/department-computing-technologies#people-academic-staff",
        "https://www.swinburne.edu.au/about/our-structure/organisational-structure/schools-departments/school-science-computing-engineering-technologies/department-engineering-technologies#people-academic-staff"
    ]

    all_profs = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        all_profs += soup.find('tbody').find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSwinburne University of Technology done...\n")
    return faculty_data


if __name__ == '__main__':
    swinburne_uni()

