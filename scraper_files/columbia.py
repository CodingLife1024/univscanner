import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

university = "Columbia University"
country = "USA"

faculty_data = []

def get_name(prof):
    name = prof.find('span', class_="faculty-name").get_text().strip()
    return name

def get_link(prof):
    link = prof.find('span', class_="faculty-name").find('a')['href']
    return link

def get_research(prof):
    research = prof.find('div', class_="faculty-interests").get_text().strip() if prof.find('div', class_="faculty-interests") else "Not Found"
    return research

def get_email(prof):
    email = prof.find('a', href=lambda href: href and href.startswith("mailto:"))
    if email is not None:
        email = email.get_text().strip()
    else:
        email = "N/A"
    return email

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_research = executor.submit(get_research, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        research = future_research.result()
        email = future_email.result()

    found_keyword = any(keyword.lower() in research.lower() for keyword in keyword_list)

    pers_links = prof.find('div', class_="faculty-links").find_all('a')
    if pers_links:
        pers_links = [link['href'] for link in pers_links][0]
    else:
        pers_links = get_scholar_profile(name)

    if found_keyword:
        print([university, country, name, email, link, pers_links])
        faculty_data.append([university, country, name, email, link, pers_links])


def columbia():
    url = "https://www.cs.columbia.edu/people/faculty/"   # homepage url
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)

    # getting the soup by parsing the html parsel to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    # d gives the array of all profs on the dept homepage
    all_profs = soup.find_all('div', class_="faculty-details")

    #iterating for every prof
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Columbia University done...")
    print()

    return faculty_data

# columbia()