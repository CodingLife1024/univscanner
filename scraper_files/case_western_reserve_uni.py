import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Case Western Reserve University"
country = "United States"

def get_name(prof):
    name = prof.find('h2').text.strip()
    return name

def get_link(prof):
    link = "https://engineering.case.edu" + prof.find('a')['href']
    return link

def get_research(prof):
    research = prof.text
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_research = executor.submit(get_research, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")
        email = new_soup.find('a', href=re.compile(r'^mailto:')).text if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def case_western_reserve_uni():
    urls = ["https://engineering.case.edu/electrical-computer-and-systems-engineering/faculty-and-staff",
            "https://engineering.case.edu/computer-and-data-sciences/faculty-and-staff"]

    total_text = ""
    for url in urls:
        response = requests.get(url)
        total_text += response.text

    soup = BeautifulSoup(total_text, "html.parser")

    posts = ["Faculty", "Chair", "Research Faculty"]

    super_divs = soup.find_all('div', {'class': 'block block-views'})

    sub_divs = [super_div for super_div in super_divs if super_div.find('h2') and any(post in super_div.find('h2').text for post in posts)]

    all_profs = [div.find_all('div', {'class': 'person--content'}) for div in sub_divs]
    flat_all_profs = [prof for sublist in all_profs for prof in sublist]
    all_profs = flat_all_profs

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nCase Western Reserve University done...\n")
    return faculty_data


if __name__ == '__main__':
    case_western_reserve_uni()