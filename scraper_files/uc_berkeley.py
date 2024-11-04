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

u_name = "University of California, Berkeley"
country = "United States"

def get_faculty_data(prof, headers):
    name_tag = prof.find('h3').find('a')
    name = name_tag.text.strip()
    link = 'https://www2.eecs.berkeley.edu' + name_tag['href']

    # Extract the email
    email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", prof.text)
    email = email_match.group(0) if email_match else "Not Found"

    # Extract research areas
    research_areas_tag = prof.find('strong', string='Research Interests:')
    research_areas = research_areas_tag.next_sibling.strip() if research_areas_tag else "Not Found"

    # Additional logic to handle multiple research areas
    if research_areas_tag:
        research_areas = []
        for a_tag in research_areas_tag.find_next_siblings('a'):
            research_areas.append(a_tag.text.strip())
        research_areas = '; '.join(research_areas)

    found_keyword = any(re.search(re.escape(keyword), research_areas, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        personal_website_tag = new_soup.find('a', string='Personal Homepage')
        if personal_website_tag:
            personal_website = personal_website_tag.get('href')
        else:
            personal_website = get_scholar_profile(name)

            print([u_name, country, name, email, link, personal_website])
            faculty_data.append([u_name, country, name, email, link, personal_website])

def uc_berkeley():
    url = "https://www2.eecs.berkeley.edu/Faculty/Lists/CS/faculty.html"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='cc-image-list__item__content')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of California, Berkeley done...\n")
    return faculty_data


if __name__ == '__main__':
    uc_berkeley()
