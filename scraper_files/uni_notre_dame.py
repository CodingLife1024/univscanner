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

u_name = "University of Notre Dame"
country = "United States"

def get_name(prof):
    name = prof.find('h2', class_="").text.strip()
    return name

def get_link(prof):
    link = prof.find('h2', class_="").find('a')['href']
    return link

def get_title(prof):
    title = prof.find('h3', class_="is-style-plain").text.lower()
    return title

def get_research(prof):
    research = prof.find('h4', class_="is-style-plain").find_next('p').text.strip() if prof.find('h4', class_="is-style-plain") else ""
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_research = executor.submit(get_research, prof)
        future_title = executor.submit(get_title, prof)

        name = future_name.result()
        link = future_link.result()
        research = future_research.result()
        title = future_title.result()

    if ("professor" in title or "lecturer" in title) and "emerit" not in title:
        new_r = requests.get(link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip()
        research += new_soup.text

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            pers_link = get_scholar_profile(name)
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])

def uni_notre_dame():
    urls = ["https://cse.nd.edu/faculty/page/1/",
            "https://cse.nd.edu/faculty/page/2/",
            "https://cse.nd.edu/faculty/page/3/",
            "https://cse.nd.edu/faculty/page/4/",
            "https://cse.nd.edu/faculty/page/5/"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('div', class_='grid directory-grid')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Notre Dame done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_notre_dame()