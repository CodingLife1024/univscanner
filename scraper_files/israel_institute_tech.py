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

u_name = "Israel Institute of Technology"
country = "Israel"

def get_name(prof):
    name = prof.find('div', {'class': 'fm_name'}).text.strip()
    return name

def get_email(prof):
    email = prof.find('a', class_="target-email contains-image")['href'].replace('\t', '') if prof.find('a', class_="target-email contains-image") else "N/A"
    return email

def get_link(prof):
    link = prof.find('a', class_="contains-image")['href'].replace('\t', '') if prof.find('a', class_="contains-image") else "N/A"
    return link

def get_research(prof):
    research = prof.find('div', class_="fm_txt_top").find('p').text.strip()
    return research

def get_title(prof):
    title = prof.find('div', class_="fm_status").text.strip().lower()
    return title

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_research = executor.submit(get_research, prof)
        future_title = executor.submit(get_title, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        research = future_research.result()
        title = future_title.result()

    if ("professor" in title or "lecturer" in title) and "emeritus" not in title:

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def israel_institute_tech():
    url = "https://www.cs.technion.ac.il/people/faculty/index.php?index=names"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'
    }

    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='fm_card_wrapper')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nIsrael Institute of Technology done...\n")
    return faculty_data


if __name__ == '__main__':
    israel_institute_tech()