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
from components.search_expertise import search_expertise

faculty_data = []

u_name = "Rutgers-New Brunswick University"
country = "United States"

def get_faculty_data_1(prof, headers):
    name = prof.find('h2', class_="newstitle").find('span').text.strip()
    link = "https://www.cs.rutgers.edu" + prof.find('a').get('href')
    email = "N/A"
    email_spans = prof.find('span', class_=lambda x: x and any(cls.startswith("cloaked_email") for cls in x.split())).find_all('span', class_=False)
    email_components = []
    for i, span in enumerate(email_spans, 1):
        email_components.extend(span.attrs.values())

    email = email_components[0] + email_components[2] + email_components[4] + email_components[1] + email_components[3] + email_components[5]

    pers_link = get_scholar_profile(name)

    research = search_expertise(pers_link, headers)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def get_faculty_data_2(prof, headers):
    name = prof.find('a').text.strip()
    link = "https://www.cs.rutgers.edu" + prof.find('a').get('href')

    email = "N/A"
    email_spans = prof.find('span', class_=lambda x: x and any(cls.startswith("cloaked_email") for cls in x.split())).find_all('span', class_=False)
    email_components = []
    for i, span in enumerate(email_spans, 1):
        email_components.extend(span.attrs.values())

    email = email_components[0] + email_components[2] + email_components[4] + email_components[1] + email_components[3] + email_components[5]

    pers_link = get_scholar_profile(name)

    research = search_expertise(pers_link, headers)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def rutgers():
    urls = [
        "https://www.cs.rutgers.edu/people/professors",
        "https://www.cs.rutgers.edu/people/affiliated-faculty",
        "https://www.cs.rutgers.edu/people/lecturers",
        "https://www.cs.rutgers.edu/people/researchers"
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    # urls 1 and 2

    urlss = [urls[0], urls[1]]

    total_text_1 = ""

    for url in urlss:
        r = requests.get(url, headers=headers)
        total_text_1 += r.text

    soup = BeautifulSoup(total_text_1, "html.parser")

    all_profs = soup.find_all('div', {'class': 'news'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_1, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    # urls 3 and 4

    urlss = [urls[2], urls[3]]

    total_text_2 = ""

    for url in urlss:
        r = requests.get(url, headers=headers)
        total_text_2 += r.text

    soup = BeautifulSoup(total_text_2, "html.parser")

    all_profs = soup.find_all('div', {'class': 'news'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data_2, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nRutgers-New Brunswick University done...\n")
    return faculty_data


if __name__ == '__main__':
    rutgers()