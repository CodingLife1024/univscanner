import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import unidecode as unidecode

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

university = "Nanyang Technological University"
country = "Singapore"

def get_faculty_data(prof):
    a_tag = prof.find('a')
    if a_tag:
        # Extract the text and the 'href' attribute value
        name = a_tag.get_text(strip=True)
        link = a_tag['href']
        dept = prof.find('span', class_='interests').get_text(strip=True) if prof.find('span', class_='interests') else "N/A"
        found_keyword = any(keyword.lower() in dept.lower() for keyword in keyword_list)

        if found_keyword:
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, 'html.parser')

            a_tag = new_soup.find('a', href=lambda href: href and href.startswith("mailto:"))

            if a_tag:
                email = a_tag.get_text(strip=True)
            else:
                email = "N/A"

            web_tag = new_soup.find('span', string='Website')

            if web_tag:
                aa_tag = web_tag.find_parent('a')

                if aa_tag:
                    pers_link = aa_tag['href']
                else:
                    pers_link = get_scholar_profile(name)

            print([university, country, name, email, link, pers_link])
            faculty_data.append([university, country, name, email, link, pers_link])

def ntus():
    url = "https://www.ntu.edu.sg/computing/our-people/faculty"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('div', class_='img-card__body')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Nanyang Technological University done...")
    print()
    return faculty_data

if __name__ == "__main__":
    ntus()