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

university = "University of Chicago"
country = "United States"

def get_faculty_data(prof):
    name_element = prof.find('h3', class_='card__title')
    name = name_element.text.strip() if name_element else "Name not found"
    url_element = prof.find('a', class_='card__url')
    url = url_element['href'] if url_element else "URL not found"
    new_response = requests.get(url)
    new_soup = BeautifulSoup(new_response.text, "html.parser")

    email_element = new_soup.find('div', class_='person-detail__value')
    email = email_element.get_text() if email_element else "N/A"

    found_keyword = any(re.search(re.escape(keyword), new_response.text) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([university, country, name, email, url, pers_link])
        print([university, country, name, email, url, pers_link])

def uchicago():
    url = "https://www.cs.uchicago.edu/people/faculty/"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('div', class_='card card--person')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Chicago done...\n")
    return faculty_data


if __name__ == '__main__':
    uchicago()
