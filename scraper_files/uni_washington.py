import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

u_name = "University of Washington"
country = "United States"

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

def get_name(prof):
    name = prof.find('div', class_='directory-name').text.strip()
    return name

def get_link(prof):
    link = prof.find('div', class_='directory-name').find('a').text.strip() if prof.find('div', class_='directory-name').find('a') else None
    return link

def get_email(prof):
    email = prof.find('div', class_='directory-email').text.strip()
    return email[:-17] + "@cs.washington.edu"

def get_research(prof):
    research = prof.find('div', class_='directory-research-interests').text.strip()
    return research

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)
        future_research = executor.submit(get_research, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()
        research = future_research.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

    return faculty_data


def uni_washington():
    url = "https://www.cs.washington.edu/people/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='row directory-row')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    return faculty_data


if __name__ == "__main__":
    uni_washington()