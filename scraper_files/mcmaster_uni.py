import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "McMaster University"
country = "Canada"

def get_name(prof):
    name = prof.find('h2', class_="faculty-card__name").get_text().strip()
    return name

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_email(new_soup):
    email = new_soup.find('a', href=re.compile(r'^mailto:')).get_text().strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else None
    return email

def get_research(new_soup):
    research = new_soup.find('div', class_="single-faculty__taxs-faculty-expertise").get_text() if new_soup.find('div', class_="single-faculty__taxs-faculty-expertise") else new_soup.text
    return research

def get_pers_link(new_soup):
    pers_link = new_soup.find_all('div', class_="single-faculty__contact__option-content")[1].find_all('a')[0]['href'] if new_soup.find_all('div', class_="single-faculty__contact__option-content")[1].find_all('a') else None
    return pers_link

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_pers_link = executor.submit(get_pers_link, new_soup)
        future_research = executor.submit(get_research, new_soup)
        future_email = executor.submit(get_email, new_soup)

        # Collect the results as they complete
        research = future_research.result()
        pers_link = future_pers_link.result()
        email = future_email.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword or True:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def mcmaster_uni():
    urls = ['https://www.eng.mcmaster.ca/faculty-staff/faculty-directory/?filter-search=&filter-research-cluster=&filter-department=56#faculty-listing__filter',
            "https://www.eng.mcmaster.ca/faculty-staff/faculty-directory/?pg=2&filter-search&filter-research-cluster&filter-department=56",
            'https://www.eng.mcmaster.ca/faculty-staff/faculty-directory/?pg=3&filter-search&filter-research-cluster&filter-department=56',
            "https://www.eng.mcmaster.ca/faculty-staff/faculty-directory/?pg=4&filter-search&filter-research-cluster&filter-department=56",
            "https://www.eng.mcmaster.ca/faculty-staff/faculty-directory/?filter-search=&filter-research-cluster=&filter-department=58#faculty-listing__filter",
            "https://www.eng.mcmaster.ca/faculty-staff/faculty-directory/?pg=2&filter-search&filter-research-cluster&filter-department=58",
            "https://www.eng.mcmaster.ca/faculty-staff/faculty-directory/?pg=3&filter-search&filter-research-cluster&filter-department=58"]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('article', class_="faculty-card")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("McMaster University done...")
    print()

    return faculty_data

if __name__ == '__main__':
    mcmaster_uni()