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

u_name = "University of Helsinki"
country = "Finland"

def get_name(prof):
    name = prof['first-name'] + " " + prof['last-name']
    return name

def get_link(prof):
    link = "https://www.helsinki.fi" + prof['url']
    return link

def get_email(prof):
    email = prof['email']
    return email

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
    research = new_r.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    pers_link = get_scholar_profile(name)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_helsinki():
    url = "https://www2.helsinki.fi/en/faculty-of-science/research-and-teaching-staff-computer-science"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    professors = soup.find_all('hy-accordion-item', accordiontitle='Professors')
    assistant_and_associate_professors = soup.find_all('hy-accordion-item', accordiontitle='Assistant and associate professors')
    lecturers = soup.find_all('hy-accordion-item', accordiontitle='University lecturers')
    researchers = soup.find_all('hy-accordion-item', accordiontitle='University researchers')

    all_sections = professors + assistant_and_associate_professors + lecturers

    for section in all_sections:
        all_profs = section.find_all('hy-person-card')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error occurred: {e}")

    print("\nUniversity of Helsinki done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_helsinki()