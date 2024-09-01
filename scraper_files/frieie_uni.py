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

u_name = "Freie Universität Berlin"
country = "Germany"

def get_name(prof):
    name = prof.find('h3', class_="box-teaser-extended-title").get_text().strip()
    return name

def get_link(prof):
    link_tag = prof.find('a', class_="box-teaser-extended")['href']
    if link_tag[0] == '/':
        link = "https://www.mi.fu-berlin.de" + link_tag
    else:
        link = link_tag
    return link

def get_research(prof):
    research = prof.find('p').get_text().strip()
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_research = executor.submit(get_research, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')
        email_tag = new_soup.find('div', class_='box-staff-table-label col-s-4', string="E-Mail")
        if email_tag:
            email = email_tag.find_next('a')['href'][7:]
        else:
            email = "N/A"
        pers_link = get_scholar_profile(name)

        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def frieie_uni():
    url = "https://www.mi.fu-berlin.de/en/inf/research/faculty/index.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('div', class_='box box-teaser-cms-3')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Freie Universität Berlin done...")
    print()

    return faculty_data

if __name__ == '__main__':
    frieie_uni()