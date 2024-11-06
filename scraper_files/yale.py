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

university = "Yale University"
country = "United States"

def get_faculty_data(prof):
    name = prof.find('a', class_="username").text.strip()
    url = "https://cpsc.yale.edu" + prof.find('a')['href']
    # new_r = requests.get(url)
    # new_soup = BeautifulSoup(new_r.text, 'html.parser')
    email = prof.find('a', href=re.compile(r'mailto:')).text.strip() if prof.find('a', href=re.compile(r'mailto:')) else "N/A"

    pers_site = prof.find('a', string='Website')['href'] if prof.find('a', string='Website') else "N/A"
    if pers_site != "N/A":
        try:
            new_r = requests.get(pers_site)
            new_soup = BeautifulSoup(new_r.text, 'html.parser')
            pers_text = new_soup.text

            site_r = requests.get(url)
            site_soup = BeautifulSoup(site_r.text, 'html.parser')
            site_text = site_soup.text

            found_keyword = any(re.search(re.escape(keyword), (pers_text + site_text).lower()) for keyword in keyword_list)

            if found_keyword:
                print([university, country, unidecode(name), email, url, pers_site])
                faculty_data.append([university, country, unidecode(name), email, url, pers_site])
        except:
            return

def yale():
    url = "https://cpsc.yale.edu/people/faculty"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all all_profs containing professor information
    all_profs = soup.find_all('tr', class_=re.compile(r'clickable'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nYale University done...\n")
    return faculty_data


if __name__ == "__main__":
    yale()