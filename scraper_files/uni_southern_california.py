import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

u_name = "University of Southern California"
country = "United States"

faculty_data = []

def get_name(prof):
    name = prof.find('h5', class_='resultName').text.strip()
    return name

def get_link(prof):
    link = "https://www.cs.usc.edu" + prof.get('href')
    return link

def get_email(new_soup):
    email = "N/A"

    email_li = new_soup.find('li', string=lambda text: text and text.strip().endswith("@usc.edu"))
    if email_li:
        email = email_li.text.strip()

    return email

def get_personal_link(new_soup, name):
    pers_link = new_soup.find('a', string='Personal Website')['href'] if new_soup.find('a', string='Personal Website') else get_scholar_profile(name)
    return pers_link

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link, headers=headers)
    new_soup = BeautifulSoup(new_r.text, 'html.parser')

    research = new_r.text

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_pers_link = executor.submit(get_personal_link, new_soup, name)
        future_email = executor.submit(get_email, new_soup)

        # Collect the results as they complete
        pers_link = future_pers_link.result()
        email = future_email.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_southern_california():
    url = "https://www.cs.usc.edu/directory/faculty/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find('div', class_='resultsModule').find_all('a')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Southern California done...")
    print()

    return faculty_data


if __name__ == '__main__':
    uni_southern_california()