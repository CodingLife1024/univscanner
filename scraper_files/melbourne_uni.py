import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "University of Melbourne"
country = "Australia"

def get_faculty_data(prof):
    name_cell = prof.find('td', headers='acad_name')
    surname_cell = prof.find('td', headers='acad_surname')
    link_cell = prof.find('td', headers='acad_profile')
    email_cell = prof.find('td', headers='acad_email')

    if name_cell and surname_cell and email_cell and link_cell:
        name = name_cell.get_text(strip=True)
        surname = surname_cell.get_text(strip=True)
        link = link_cell.find('a').get('href') if link_cell.find('a') else None
        email = email_cell.find('a').get('href').replace('mailto:', '')

        name = name + " " + surname

        if link:
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            research_areas = []
            tags = new_soup.find_all('div', class_='research-area-tag')
            for tag in tags:
                research_areas.append(tag.get_text(strip=True))
            research = ', '.join(research_areas)

            found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                pers_link = get_scholar_profile(name)
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])

def melbourne_uni():
    url = "https://cis.unimelb.edu.au/people"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    all_categories = soup.find_all('h2', {'class': 'title'})

    all_profs = []

    for category in all_categories:
        if category.text.strip() == "Academic staff":
            table = category.find_next_sibling('table')
            all_profs.extend(table.find_all('tr'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Melbourne done...")
    print()
    return faculty_data



if __name__ == "__main__":
    melbourne_uni()
