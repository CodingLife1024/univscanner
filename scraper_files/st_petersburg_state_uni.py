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

u_name = "Saint Petersburg State University"
country = "Russia"

def get_name(prof):
    name = prof.find('a').text.strip()
    return name

def get_link(prof):
    link = "https://math-cs.spbu.ru" + prof.find('a')['href']
    return link

def get_email(new_soup):
    email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip() if new_soup.find('a', href=re.compile(r"^mailto:")) else "N/A"
    return email

def get_research(new_soup):
    research = new_soup.text
    return research

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link, headers=headers, verify=False)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_email = executor.submit(get_email, new_soup)
        future_research = executor.submit(get_research, new_soup)

        email = future_email.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = new_soup.find('nodindex').find('a')['href'] if new_soup.find('nodindex') else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def st_petersburg_state_uni():
    urls = ["https://math-cs.spbu.ru/en/people/"]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'}

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers, verify=False)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_="col-sm-12 col-md-4 col-lg-2 teachers")
    print(len(all_profs))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Saint Petersburg State University done...")
    print()

    return faculty_data


if __name__ == '__main__':
    st_petersburg_state_uni()