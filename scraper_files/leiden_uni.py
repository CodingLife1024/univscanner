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

u_name = "Leiden University"
country = "Netherlands"

def get_name(name_tag):
    return name_tag.get_text().strip()

def get_title(title_tag):
    return title_tag.get_text().strip()

def get_link(link_tag):
    return "https://www.universiteitleiden.nl" + link_tag['href']

def get_faculty_data(prof):
    link_tag = prof.find('a')
    name_tag = prof.find('strong')
    title_tag = prof.find('span')

    if link_tag and name_tag and title_tag:
        with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
            future_name = executor.submit(get_name, name_tag)
            future_link = executor.submit(get_link, link_tag)
            future_title = executor.submit(get_title, title_tag)

            # Collect the results as they complete
            name = future_name.result()
            link = future_link.result()
            title = future_title.result()

        if "emeritus" not in title.lower():
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, 'html.parser')
            research = new_r.text
            email = new_soup.find('dt', string='E-mail').find_next('dd').get_text().strip() if new_soup.find('dt', string='E-mail') else "N/A"

            found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                pers_link = get_scholar_profile(name)
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])

def leiden_uni():
    url = "https://www.universiteitleiden.nl/en/science/computer-science/staff"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    profs = soup.find_all('section')[:2]
    all_profs_super = [prof.find_all('li') for prof in profs]

    all_profs = [item for sublist in all_profs_super for item in sublist]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Leiden University done...")
    print()

    return faculty_data

if __name__ == '__main__':
    leiden_uni()