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
from unidecode import unidecode

university = "Oxford University"
country = "United Kingdom"

def normalize_email(email):
    # Replace common variations with '@'
    email = re.sub(r'\s+at\s+', '@', email)
    email = re.sub(r'\s*\(\s*a\s*\)\s*', '@', email)
    email = re.sub(r'\s*\{\s*at\s*\}\s*', '@', email)
    email = re.sub(r'\s*\(dot\)\s*', '.', email)
    email = re.sub(r'\s*\{\s*dot\s*\}\s*', '.', email)
    email = re.sub(r'\s*\[\s*dot\s*\]\s*', '.', email)
    return email

def get_name(prof):
    name = prof.get_text().strip()
    return name

def get_link(prof):
    href = "https://www.cs.ox.ac.uk/people/" + unidecode(prof).lower().replace(" ", ".")
    return href

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    new_resonse = requests.get(link)
    new_content = new_resonse.text

    new_soup = BeautifulSoup(new_content, 'html.parser')

    if any(keyword in new_soup.get_text().lower() for keyword in keyword_list):
        pers_link = get_scholar_profile(name)

        try:
            email = new_soup.find('div', class_='scaled-text', itemprop='email').get_text()[3:]
            email = normalize_email(email)
        except AttributeError:
            email = "N/A"

        faculty_data.append([university, country, name, email, link, pers_link])
        print([university, country, unidecode(name), email, link, pers_link])

def oxford():
    url = "https://www.cs.ox.ac.uk/people/faculty.html"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('span', itemprop='name')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Oxford University done....")
    print()
    return faculty_data

if __name__ == "__main__":
    oxford()