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

u_name = "Purdue University"
country = "United States"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip() if len(columns) > 0 else None
    email = None
    if len(columns) > 4 and columns[4].find('a'):
        email = columns[4].find('a')['href'].replace('mailto:', '')
    link = None
    if len(columns) > 5 and columns[5].find('a'):
        link = "https://www.cs.purdue.edu/people/faculty/" + columns[5].find('a')['href']

    if link is not None:
        new_r = requests.get(link)
        research = new_r.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def purdue_uni():
    url = "https://www.cs.purdue.edu/people/faculty/index.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table_professor = soup.find('table', class_='directory table table-bordered table-striped table-condensed')

    all_profs = table_professor.find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Purdue University done...")
    print()
    return faculty_data


if __name__ == "__main__":
    purdue_uni()