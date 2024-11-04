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

university = "Princeton University"
country = "United States"

def get_faculty_data(prof):
    name = prof.find('a').get_text()
    link = "https://www.cs.princeton.edu" + prof.find('a')['href']
    pers_link = prof.find('a', class_='btn btn-xs btn-default')['href'] if prof.find('a', class_='btn btn-xs btn-default') else "Not Found"
    email = link[44:] + "@cs.princeton.edu"

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")    # getting the soup of the prof's page

    pers_r = requests.get(pers_link)
    pers_soup = BeautifulSoup(pers_r.text, "html.parser") if pers_link != "Not Found" else None

    research_text = new_soup.text
    pers_text = pers_soup.text if pers_soup else None

    found_keyword = any(re.search(re.escape(keyword), research_text + pers_text) for keyword in keyword_list)

    if found_keyword:
        print([university, country, name, email, link, pers_link])
        faculty_data.append([university, country, name, email, link, pers_link])

def princeton():
    url = "https://www.cs.princeton.edu/people/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='person-details')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPrinceton University done...\n")
    return faculty_data


if __name__ == "__main__":
    princeton()