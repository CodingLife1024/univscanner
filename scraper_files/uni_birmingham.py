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

u_name = "University of Birmingham"
country = "United Kingdom"

def get_name(prof):
    name = " ".join(prof.find('h3').find('a').get_text().strip().split(" ")[1:])
    return name

def get_link(prof):
    link = 'https://www.birmingham.ac.uk' + prof.find('h3').find('a').get('href')
    return link

def get_email(prof):
    email_tag = prof.find('a', href=lambda x: x and x.startswith("mailto:"))
    if email_tag:
        email = email_tag.get_text().strip()
    else:
        email = "N/A"
    return email

def get_research(new_soup):
    research = new_soup.find('div', {'class': 'content'}).text.strip() if new_soup.find('div', {'class': 'content'}) else ""
    return research

def get_personal_link(new_soup, name):
    pers_link_tag = new_soup.find('a', string=re.compile("personal", re.IGNORECASE))
    if pers_link_tag:
        pers_link = pers_link_tag['href']
    else:
        pers_link = get_scholar_profile(name)
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
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_research = executor.submit(get_research, new_soup)
        future_pers_link = executor.submit(get_personal_link, new_soup, name)

        research = future_research.result()
        pers_link = future_pers_link.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_birmingham():
    url = "https://www.birmingham.ac.uk/schools/computer-science/people/index.aspx"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('article', {'class':"media staff media--flipped"})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Birmingham done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_birmingham()