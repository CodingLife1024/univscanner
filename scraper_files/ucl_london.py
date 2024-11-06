import requests
from bs4 import BeautifulSoup
import sys
import os
import re
from unidecode import unidecode
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

university = "UCL London"
country = "United Kingdom"

def get_faculty_data(prof):
    columns = prof.find_all('td')
    name = columns[0].text.strip()
    role = columns[1].text.strip()
    email = columns[2].find('a').text.strip()
    url = columns[0].find('a')['href']

    new_soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    research_text = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), (research_text + role).lower()) for keyword in keyword_list)
    
    if found_keyword:
        pers_link = get_scholar_profile(name)
        print([university, country, unidecode(name), email, url, pers_link])
        faculty_data.append([university, country, unidecode(name), email, url, pers_link])

def ucl_london():
    url = "https://www.ucl.ac.uk/computer-science/people/computer-science-academic-staff"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = []

    # Find all tables containing professor information
    tables = soup.find_all('table')

    # Iterate through each table
    for table in tables:
        rows = table.find_all('tr')[1:]
        all_profs.extend(rows)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUCL London done...\n")
    return faculty_data


if __name__ == '__main__':
    ucl_london()