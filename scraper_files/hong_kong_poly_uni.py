import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

u_name = "Honk Kong Polytechnic University"
country = "Hong Kong"

faculty_data = []

def get_name(prof):
    return prof.find('span', class_="ppl-detail-blk__name").text.strip()

def get_link(prof):
    link = prof.find('div', class_="ppl-detail-blk__img-ctrl").find('a').get('href') if prof.find('div', class_="ppl-detail-blk__img-ctrl") else None
    return f"https://www.polyu.edu.hk{link}" if link else None

def get_email(prof):
    return prof.find('span', class_="ico-mail").find_next('a').text.strip() if prof.find('span', class_="ico-mail") else None

def get_personal_link(prof, name):
    pers_link = prof.find('span', class_="ico-global").find_next('a').get('href') if prof.find('span', class_="ico-global") else get_scholar_profile(name)
    return pers_link

def get_research(full_link):
    new_r = requests.get(full_link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.find('div', class_='static-content').text.strip() if new_soup.find('div', class_='static-content') else None
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        # Collect results
        name = future_name.result()
        full_link = future_link.result()
        email = future_email.result()

        # Get research and personal link in parallel
        future_research = executor.submit(get_research, full_link)
        future_pers_link = executor.submit(get_personal_link, prof, name)

        research = future_research.result()
        pers_link = future_pers_link.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        print([u_name, country, name, email, full_link, pers_link])
        faculty_data.append([u_name, country, name, email, full_link, pers_link])

def hong_kong_poly_uni():
    url = "https://www.polyu.edu.hk/comp/people/academic-staff/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    all_profs = soup.find_all('div', class_='ppl-detail__item')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nHong Kong Polytechnic University done...\n")
    return faculty_data

if __name__ == "__main__":
    hong_kong_poly_uni()
