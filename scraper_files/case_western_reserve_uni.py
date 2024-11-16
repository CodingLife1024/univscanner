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

def get_faculty_data(prof):
    name = prof.find('a').text.strip()
    link = "https://engineering.case.edu" + prof.find('a')['href']

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        email = new_soup.find('a', href=re.compile(r'^mailto:')).get_text().strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"
        pers_link = new_soup.find('div', class_="view-content").find('a')['href'] if new_soup.find('div', class_="view-content").find('a') else get_scholar_profile(name)
        if pers_link[0] == '/':
            pers_link = "https://engineering.case.edu" + pers_link
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

    all_profs = soup.find_all('div', class_="person--content")

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