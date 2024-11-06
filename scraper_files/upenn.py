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

university = "University of Pennsylvania"
country = "United States"

def get_faculty_data(prof):
    name = prof.find('div', class_='StaffListName').text.strip()
    site = prof.find('a')['href'].strip()
    email_a_tag = prof.find('a', href=lambda href: href and href.startswith("mailto:"))

    if email_a_tag:
        email = email_a_tag['href'].replace('mailto:', '')

    expertise = prof.find('div', class_='StaffListTitles').text.strip()

    new_r = requests.get(site)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    pers_site = new_soup.find('a', string='Personal Website')['href'] if new_soup.find('a', string='Personal Website') else "N/A"

    if pers_site != "N/A":
        try:
            pers_r = requests.get(pers_site)
            pers_soup = BeautifulSoup(pers_r.text, 'html.parser')
            pers_text = pers_soup.text
        except:
            return

    else:
        pers_soup = None
        pers_text = ""

    found_keyword = False

    if pers_soup:
        found_keyword = any(re.search(re.escape(keyword), (pers_text + expertise).lower()) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([university, country, name, email, site, pers_site])
        print([university, country, name, email, site, pers_site])

def upenn():
    url = "https://directory.seas.upenn.edu/computer-and-information-science/"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all(class_=re.compile(r'col-12.*SingleStaffList.*ft-cis'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity of Pennsylvania done...\n")
    return faculty_data


if __name__ == "__main__":
    upenn()