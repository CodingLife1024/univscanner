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

u_name = "University of Massachusetts"
country = "United States"

def get_name(prof):
    name = prof.find('div', class_="person__title").text.strip()
    return name

def get_link(prof):
    link = "https://www.cics.umass.edu" + prof.find('a')['href']
    return link

def get_email(prof):
    email = prof.find('a', href=re.compile(r"^mailto:")).text.strip() if prof.find('a', href=re.compile(r"^mailto:")) else "N/A"
    return email

def get_title(prof):
    title = prof.find('div', class_="person__role").text.lower()
    return title


def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_title = executor.submit(get_title, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        title = future_title.result()

    if ("professor" in title or "lecturer" in title) and "emerit" not in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        research = new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_massachusetts():
    url = "https://www.cics.umass.edu/about/directory"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'person--card-long'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Massachusetts done...\n")
    return faculty_data


if __name__ == '__main__':
    uni_massachusetts()