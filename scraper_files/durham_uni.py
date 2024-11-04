import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

u_name = "Durham University"
country = "United Kingdom"

faculty_data = []

def get_name_and_link(prof):
    anchor_tag = prof.find('a')
    if anchor_tag:
        name = " ".join(anchor_tag.text.split(" ")[1:])
        link = "https://www.durham.ac.uk" + anchor_tag['href']
        return name, link
    return False, False

def get_email(new_soup):
    email_tag = new_soup.find('a', href=lambda x: x and x.startswith("mailto:"))
    if email_tag:
        email = email_tag['href'][7:]
        return email
    return False

def get_research(new_soup):
    biography_tag = new_soup.find('h3', id="biography")
    if biography_tag:
        biography = biography_tag.find_next('div').text.strip()
    else:
        biography = ""

    research_interests_tag = new_soup.find('h3', id="research-interests")
    if research_interests_tag:
        research_interests = research_interests_tag.find_next('div').text.strip()
    else:
        research_interests = ""

    research = biography + research_interests
    return research

def get_personal_link(new_soup, name):
    pers_link = new_soup.find('a', string="Personal website") if new_soup.find('a', string="Personal website") else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    name, link = get_name_and_link(prof)
    if not name:
        return
    else:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_email = executor.submit(get_email, new_soup)
            future_research = executor.submit(get_research, new_soup)
            future_pers_link = executor.submit(get_personal_link, new_soup, name)

            email = future_email.result()
            research = future_research.result()
            pers_link = future_pers_link.result()

        if email:
            found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
            if found_keyword:
                faculty_data.append([u_name, country, name, email, link, pers_link])
                print([u_name, country, name, email, link, pers_link])


def durham_uni():
    url = "https://www.durham.ac.uk/departments/academic/computer-science/about-us/staff/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    academic_staff = soup.find('h2', string="Academic Staff").find_next('table').find_all('td')
    research_staff = soup.find('h2', string="Research Staff").find_next('table').find_all('td')

    all_profs = academic_staff + research_staff

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nDurham University done...\n")
    return faculty_data

if __name__ == "__main__":
    durham_uni()
