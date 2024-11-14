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

def get_faculty_data(prof, headers):
    name = prof.find('a').get_text().strip()
    link = "https://www.cs.ox.ac.uk" + prof.find('a')['href']

    new_resonse = requests.get(link, headers=headers)
    new_content = new_resonse.text

    new_soup = BeautifulSoup(new_content, 'html.parser')

    found_keyword = any(keyword in new_soup.get_text().lower() for keyword in keyword_list)

    if found_keyword or True:
        pers_link = new_soup.find('h2', class_="panel-subheading text-uppercase no-top-margin").find_next('a')['href'] if new_soup.find('h2', class_="panel-subheading text-uppercase no-top-margin") else get_scholar_profile(name)
        if pers_link.startswith("/"):
            pers_link = "https://www.cs.ox.ac.uk" + pers_link
        try:
            email = new_soup.find('div', class_='scaled-text', itemprop='email').get_text()[3:]
            email = normalize_email(email)
        except AttributeError:
            email = "N/A"

        faculty_data.append([university, country, name, email, link, pers_link])
        print([university, country, unidecode(name), email, link, pers_link])

def oxford():
    url = "https://www.cs.ox.ac.uk/people/faculty.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = []

    super_class = soup.find_all('ul', class_='list-unbulleted')

    for i in super_class:
        profs = i.find_all('li')
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nOxford University done...\n")
    return faculty_data


if __name__ == "__main__":
    oxford()