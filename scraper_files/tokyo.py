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

university = "University of Tokyo"
country = "Japan"

def get_faculty_data(prof):
    cols = prof.find_all('td')
    if len(cols) == 2:
        name_col = cols[0]
        research_col = cols[1]

        # Extract the name and link
        name_tag = name_col.find('a')
        name = name_tag.get_text(strip=True)
        link = name_tag['href']

        # Extract the research area
        research_area = research_col.get_text(strip=True)

        # Append the extracted data to the list
        found_keyword = any(re.search(re.escape(keyword), research_area.lower()) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([university, country, name, 'N/A', link, pers_link])
            print([university, country, name, 'N/A', link, pers_link])

def tokyo():
    url = "https://www.i.u-tokyo.ac.jp/edu/course/cs/members_e.shtml"  # homepage url

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find the table
    table = soup.find('table')

    all_profs = table.find_all('tr')[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Tokyo done...\n")
    return faculty_data

if __name__ == '__main__':
    tokyo()
