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

u_name = "University of Rochester"
country = "United States"

def get_name(prof):
    name = prof.find('h4').get_text().strip()
    return name

def get_link(prof):
    if prof.find('h4').find('a'):
        link = "https://www.cs.rochester.edu/people/faculty" + prof.find('h4').find('a')['href']
    else:
        return None
    return link

def get_title(prof):
    title = prof.find('p', class_="position").get_text().strip()
    return title

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:')).get_text().strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    return email

def get_pers_link(prof, name):
    pers_link = prof.find('a', string='Website')['href'] if prof.find('a', string='Website') else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        title = future_title.result()
        email = future_email.result()

    if "student" in title.lower() or "emeritus" in title.lower() or link == None:
        return

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_pers_link(prof, name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def uni_rochester():
    url = "https://www.cs.rochester.edu/people/index.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('article', class_="person person-row has-picture")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity of Rochester done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_rochester()
