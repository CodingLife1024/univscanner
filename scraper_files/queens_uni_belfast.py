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

u_name = "Queens University Belfast"
country = "United Kingdom"

def get_name(prof):
    name = prof.text
    name = name.replace("Dr", "").replace("Professor", "").replace("Dr.", "").replace("Prof.", "").strip()
    name_parts = name.split(",")
    name = (name_parts[1] + " " + name_parts[0]).strip()
    return name

def get_link(prof):
    link = "https://www.qub.ac.uk" + prof.find('a')['href']
    return link

def get_email(prof):
    email_parts = prof['title'].split(" ")
    email = "N/A"
    for part in email_parts:
        if "@" in part:
            email = part
            break
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def queens_uni_belfast():
    urls = ["https://www.qub.ac.uk/schools/eeecs/Connect/Staff/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    titles = ["Professors", "Professors (Education)", "Senior Lecturers", "Lecturers", "Senior Lecturers (Education)", "Lecturers (Education)"]

    super_class = soup.find_all('h4', string=lambda s: s is not None and s.strip() in titles)

    all_profs = []

    for s in super_class:
        table = s.find_next('table').find_all('span')
        all_profs.extend(table)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nQueens University Belfast done...\n")
    return faculty_data


if __name__ == '__main__':
    queens_uni_belfast()


