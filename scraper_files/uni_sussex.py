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

u_name = "University of Sussex"
country = "United Kingdom"

def get_faculty_data(prof):
    name = prof.find('span', class_="people-name").text.strip()
    link = "https://www.sussex.ac.uk" + prof['href']
    title = prof.find('span', class_="people-title").text.strip().lower()

    if ("professor" in title or "leturer" in title) and "emeritus" not in title:
        new_r = requests.get(link)

        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_sussex():
    urls = ["http://www.sussex.ac.uk/informatics/people/peoplelists/group/teaching-faculty",
            "https://www.sussex.ac.uk/schools/engineering-and-informatics/contacts/informatics/group/research-faculty"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('a', {'class': 'people-card-link'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Sussex done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_sussex()