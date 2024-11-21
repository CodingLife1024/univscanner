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

u_name = "City University Hong Kong"
country = "Hong Kong"

faculty_data = []

def get_faculty_data(prof):
    name = prof.find('div', class_="name").get_text().strip() if prof.find('div', class_="name") else "Name not found"
    name = name.split(" ")[1:-1]
    name = " ".join(name)
    name_parts = name.split(",")
    name = name_parts[1] + " " + name_parts[0] if len(name_parts) > 1 else name_parts[0]
    name = name.title()
    profile = prof.find('div', class_="profile")
    links = profile.find_all('a')
    email = links[0]['href'][7:] if links[0] else "Email not found"
    link = links[1]['href'] if links[1] else "Link not found"
    research = prof.find('div', class_="interest").text[22:].strip() if prof.find('div', class_="interest") else "N/A"
    found_keyword = any(re.search(re.escape(keyword), research.lower(), re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        personal_webpage = None
        other_links_section = new_soup.find('h2', class_='subheader', string="Other Links")
        if other_links_section:
            links = other_links_section.find_next('li').find('a')['href']
            personal_webpage = links if links else None

        if not personal_webpage:
            personal_webpage = get_scholar_profile(name)

        faculty_data.append([u_name, country, name, email, link, personal_webpage])
        print([u_name, country, name, email, link, personal_webpage])

def city_uni_hk():
    url_1 = "https://www.cs.cityu.edu.hk/people/academic-staff"
    url_2 = "https://www.cs.cityu.edu.hk/people/teaching-staff"

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)
    html_content = response_1.text + response_2.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('article', class_='person-card')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nCity University Hong Kong done...\n")
    return faculty_data


if __name__ == '__main__':
    city_uni_hk()