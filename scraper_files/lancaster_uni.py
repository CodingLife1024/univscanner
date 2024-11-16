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

u_name = "Lancaster University"
country = "United Kingdom"

def get_name(prof):
    name = prof.find('h3', class_="name").get_text().replace("Dr", "").replace("Professor", "").strip()
    return name

def get_link(prof):
    link = "https://www.lancaster.ac.uk" + prof.find('a')['href']
    return link

def get_title(prof):
    title = prof.find('span', class_="job-title").get_text().strip()
    return title

def get_email(prof):
    obfuscated_email_element = prof.find('span', class_="email").find('a')['rel'][0] if prof.find('span', class_="email") else None
    if not obfuscated_email_element:
        return
    email = obfuscated_email_element[::-1].replace("//", "@").replace("/", ".")
    return email

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        title = future_title.result()
        email = future_email.result()

    if "student" in title.lower():
        return
    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, "html.parser")
    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])


def lancaster_uni():
    url = "https://www.lancaster.ac.uk/scc/about-us/people/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='cell feature staff-row')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nLancaster University done...\n")
    return faculty_data

if __name__ == '__main__':
    lancaster_uni()