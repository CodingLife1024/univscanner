import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Lund University"
country = "Sweden"

def get_name(prof):
    name = prof.find('h4', class_="h5 header-xs").text.strip()
    return name

def get_link(prof):
    link = "https://www.lunduniversity.lu.se" + prof.find('h4', class_="h5 header-xs").find('a')['href']
    return link

def get_email(prof):
    email = prof.find('span', class_="spamspan").text.strip().replace(' [at] ', '@').replace(' [dot] ', '.')
    return email

def get_research(new_soup):
    research = new_soup.text
    return research

def get_personal_link(new_soup, name):
    pers_link = new_soup.find('span', class_="fw-semibold", string="Personal website:").find_next('a')['href'] if new_soup.find('span', class_="fw-semibold", string="Personal website:") else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_research = executor.submit(get_research, new_soup)
        future_personal_link = executor.submit(get_personal_link, new_soup, name)

        # Collect the results as they complete
        research = future_research.result()
        pers_link = future_personal_link.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def lund_uni():
    url = "https://www.lunduniversity.lu.se/lucat/group/v1000234"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_profs = soup.find_all('li', class_='border-bottom')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Lund University done...")
    print()
    return faculty_data

if __name__ == '__main__':
    lund_uni()