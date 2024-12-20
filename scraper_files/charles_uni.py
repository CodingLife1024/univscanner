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

u_name = "Charles University"
country = "Czech Republic"

def get_name(prof):
    name = prof.find('h3').text.split(",")[0].split(".")[-1].strip()
    return name

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_email(prof):
    email = prof.find('a', href=re.compile(r'^mailto:')).text.strip() if prof.find('a', href=re.compile(r'^mailto:')) else "N/A"
    return email

def get_faculty_data(prof):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_name = executor.submit(get_name, prof)
            future_link = executor.submit(get_link, prof)
            future_email = executor.submit(get_email, prof)

            name = future_name.result()
            link = future_link.result()
            email = future_email.result()

        pers_link = prof.find('a', class_="external")['href'] if prof.find('a', class_="external") else False
        research = prof.text

        new_r = requests.get(pers_link) if pers_link else requests.get(link)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        research += new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            if pers_link == False:
                pers_link = new_soup.find('a', href=re.compile(r'^mailto:')).find_next('a')['href'] if new_soup.find('a', href=re.compile(r'^mailto:')).find_next('a') else get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])
    except Exception as e:
        print(f"Error occurred: {e}")

def charles_uni():

    urls = [
        "https://cs.mff.cuni.cz/en//about-school/departments?code=d3s",
        "https://cs.mff.cuni.cz/en//about-school/departments?code=201",
        "https://cs.mff.cuni.cz/en//about-school/departments?code=202"
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers)
        total_text += r.text

    soup = BeautifulSoup(total_text, 'html.parser')

    all_profs = soup.find_all('div', {'class': 'box box-person-portrait box-person-portrait-medium'})
    all_profs_2 = soup.find_all('div', {'class': 'box box-person-portrait box-person-portrait-full'})

    all_profs = all_profs + all_profs_2

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nCharles University done...\n")
    return faculty_data


if __name__ == "__main__":
    charles_uni()