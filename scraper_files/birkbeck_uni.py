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

u_name = "Birkbeck University of London"
country = "United Kingdom"

def get_faculty_data(prof, headers):
    name = prof.find('h1', class_="h3-size").text.strip()
    link = prof['href']

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r'^mailto:')).text.strip() if new_soup.find('a', href=re.compile(r'^mailto:')) else "N/A"

    research = new_soup.text

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def birkbeck_uni():
    urls = [
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=11",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=21",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=31",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=41",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=51",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=61",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=71",
        "https://search.bbk.ac.uk/search/people/?q=&departments=School+of+Computing+and+Mathematical+Sciences&researchInterests=&businessMedia=&start_rank=81",
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

    total_text = ""

    for url in urls:
        r = requests.get(url, headers=headers)
        total_text += r.text
        print("Fetching URL..." + url + "\n")

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('a', {'class': 'row expanded'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nBirkbeck University of London done...\n")
    return faculty_data


if __name__ == "__main__":
    birkbeck_uni()