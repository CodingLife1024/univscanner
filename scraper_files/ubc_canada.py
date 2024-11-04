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

u_name = "University of British Columbia"
country = "Canada"

def get_faculty_data(prof):
    name_td = prof.find('td', {'headers': "view-field-person-lname-table-column"})
    if not name_td:
        return
    a = name_td.find('a', class_="contact-content-name")
    name = (a.get_text()).strip()
    link = 'https://www.cs.ubc.ca' + a.get('href')

    personal_page_a = name_td.find_all('a')[1] if len(name_td.find_all('a')) > 1 else None
    personal_page_link = personal_page_a.get('href') if personal_page_a else get_scholar_profile(name)

    email_td = prof.find('td', {'class': 'views-field-field-person-email'})
    email_a = email_td.find('a', href=re.compile(r'^mailto:')) if email_td else None
    email = email_a.text if email_a else "Email not found"

    research_td = prof.find('td', {'headers': "view-field-research-groups-table-column"})
    research_areas = research_td.get_text(strip=True) if research_td else "Research areas not found"

    found_keyword = any(re.search(keyword, research_areas.lower(), re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        print([u_name, country, name, email, link, personal_page_link])
        faculty_data.append([u_name, country, name, email, link, personal_page_link])

def ubc_canada():
    url = "https://www.cs.ubc.ca/people/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find('div', {'class': "view-content"}).find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of British Columbia done...\n")
    return faculty_data


if __name__ == '__main__':
    ubc_canada()
