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

u_name = "Pennsylvania State University"
country = "United States"

def get_name(prof):
    name = prof.text.strip()
    return name

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_email(new_soup):
    email = new_soup.find('a', href=lambda href: href and href.startswith("mailto:")).text.strip()
    return email

def get_research(new_soup):
    research = new_soup.find('div', class_='research').text.strip() if new_soup.find('div', class_='research') else "N/A"
    interests = new_soup.find('div', class_='interest').text.strip() if new_soup.find('div', class_='interest') else "N/A"
    department = new_soup.find('div', class_='department').text.strip() if new_soup.find('div', class_='department') else "N/A"
    research = research + interests + department
    return research

def get_personal_link(new_soup, name):
    pers_link = new_soup.find('span', id_="idDetail_lbl_WWW").find('a')['href'] if new_soup.find('span', id_="idDetail_lbl_WWW") else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_research = executor.submit(get_research, new_soup)
        future_email = executor.submit(get_email, new_soup)
        future_pers_link = executor.submit(get_personal_link, new_soup, name)

        research = future_research.result()
        email = future_email.result()
        pers_link = future_pers_link.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def penn_state_uni():
    urls = ["https://www.eecs.psu.edu/research-areas/computer-architecture.aspx",
            "https://www.eecs.psu.edu/research-areas/integrated-circuits-systems.aspx",
            "https://www.eecs.psu.edu/research-areas/operating-systems-cloud-computing.aspx"]

    all_profs = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        profs_on_page = soup.find_all('ul', {'class': 'zero'})
        for prof in profs_on_page:
            prof_li = prof.find_all('li')
            all_profs.extend(prof_li)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPennsylvania State University done...\n")
    return faculty_data

if __name__ == "__main__":
    penn_state_uni()