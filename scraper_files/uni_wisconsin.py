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

u_name = "University of Wisconsin"
country = "United States"

def get_faculty_data(prof):
    name = prof.find('h3').text.strip()
    link = prof.find('a')['href']
    email_tag = prof.find_all('a', href=True)

    email = "Email not found"
    for tag in email_tag:
        if tag["href"].startswith("mailto:"):
            email = tag["href"][7:]
            break

    try:
        new_r = requests.get(link)
        new_r.raise_for_status()

        found_keyword = any(re.search(re.escape(keyword), new_r.text, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            scholar_profile = get_scholar_profile(name)
            print([u_name, country, name, email, link, scholar_profile])
            faculty_data.append([u_name, country, name, email, link, scholar_profile])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for {name}: {e}")
        return

def uni_wisconsin():
    url = "https://www.cs.wisc.edu/people/faculty/"

    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses

        soup = BeautifulSoup(r.text, "html.parser")
        faculty_tag = soup.find_all('h2', class_=None, id=None)

        all_profs = []

        for tag in faculty_tag:
            if tag.text != "Emeritus Faculty" and tag.text != "In Memoriam":
                all_faculty = tag.find_next('div', class_="faculty-list")
                all_profs += all_faculty.find_all('div', class_="faculty-member")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error occurred: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")


    print("\nUniversity of Wisconsin done...\n")
    return faculty_data

if __name__ == "__main__":
    uni_wisconsin()