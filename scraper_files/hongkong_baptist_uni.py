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

u_name = "Hong Kong Baptist University"
country = "Hong Kong"

def get_name(prof):
    name = prof.find('h4', style=True).text.replace("Dr.", "").replace("Prof.", "").strip().title()
    return name

def get_email(prof):
    email = prof.find('i', class_="glyphicon glyphicon-envelope").find_next('script').text[14:-3] + "@comp.hkbu.edu.hk" if prof.find('i', class_="glyphicon glyphicon-envelope") else "N/A"
    return email

def get_link(prof):
    link = "https://www.comp.hkbu.edu.hk/v1/" + prof.find('a').get('href')
    return link

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

    research = new_soup.text.strip()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('i', class_="glyphicon glyphicon-globe title_icon").find_next('a')['href'] if new_soup.find('i', class_="glyphicon glyphicon-globe title_icon") else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def hongkong_baptist_uni():
    urls = ["https://www.comp.hkbu.edu.hk/v1/?page=faculty"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="col-md-3 col-sm-5 m_card")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print('\nHong Kong Baptist University done...\n')
    return faculty_data


if __name__ == '__main__':
    hongkong_baptist_uni()