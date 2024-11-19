import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

faculty_data = []

university = "Massachusetts Institute of Technology (MIT)"
country = "United States"

def get_faculty_data(name, base_url, headers, faculty_data):
    response = requests.get(base_url, headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    element = soup.find('a', class_="people-index-image", title=name)
    if not element:
        return

    text_content = element.get('title')
    href = element.get('href')
    indiv_url = href if href.startswith('http') else base_url + href

    new_response = requests.get(indiv_url, headers=headers)
    new_html_content = new_response.text
    new_soup = BeautifulSoup(new_html_content, 'html.parser')

    extract_email = new_soup.find_all('a', href=lambda href: href and href.startswith('mailto:'))
    email = extract_email[0].get_text() if extract_email else 'No Email Found'

    extract_research = new_soup.find_all('a', href=lambda href: href and href.startswith('/people/?fwp_research'))
    research_list = [link.get_text() for link in extract_research]

    pers_url = new_soup.find('a', href=lambda href: href and href.startswith('http'), string='Website')
    if pers_url:
        pers_url = pers_url.get('href')
    else:
        pers_url = get_scholar_profile(name)

    departments = ["Robotics", "Computer Architecture"]

    for department in departments:
        if department in research_list:
            print([university, country, text_content, email, indiv_url, pers_url])
            faculty_data.append([university, country, text_content, email, indiv_url, pers_url])
            break

def mit():
    base_url = "https://www.eecs.mit.edu/role/faculty/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }

    response = requests.get(base_url, headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    all_names = [element.get('title') for element in soup.find_all('a', class_="people-index-image")]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, name, base_url, headers, faculty_data) for name in all_names]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nMassachusetts Institute of Technology (MIT) done...\n")
    return faculty_data


if __name__ == "__main__":
    mit()