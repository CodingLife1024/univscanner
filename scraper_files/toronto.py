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

university = "University of Toronto"
country = "Canada"

def get_faculty_data(prof):
    columns = prof.find_all('td')

    name_tag = columns[0].find('a')
    name = name_tag.text.strip() if name_tag else 'No name found'
    website = name_tag['href'] if name_tag else 'No website found'

    email_tag = columns[1].find('a', href=True)
    email = email_tag['href'].replace('mailto:', '') if email_tag and 'mailto:' in email_tag['href'] else 'No email found'

    research_areas = columns[2].text.strip() if len(columns) > 2 else 'No research areas found'

    found_keyword = any(keyword in (research_areas).lower() for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([university, country, name, email, website, pers_link])
        print([university, country, name, email, website, pers_link])


def toronto():
    url = "https://web.cs.toronto.edu/people/faculty-directory"  # homepage URL
    r = requests.get(url)  # request to URL

    # Getting the soup by parsing the HTML parser to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the blueTable table
    blue_table = soup.find('table', class_='blueTable')

    if blue_table:
        # Find all rows in the table except the header row
        all_profs = blue_table.find_all('tr')[1:]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error occurred: {e}")

    print("\nUniversity of Toronto done...\n")
    return faculty_data


if __name__ == '__main__':
    toronto()
