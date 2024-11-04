import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint
from tqdm import tqdm

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = 'New York University'
country = 'United States'

def get_faculty_data(prof, headers):
    name_tag = prof.find('p', class_='name bold')
    if name_tag:
        name = name_tag.get_text(strip=True)
        website_tag = name_tag.find('a')
        website = website_tag['href'] if website_tag else None

        email_tag = prof.find(string=re.compile(r'Email:'))
        if email_tag:
            email = email_tag.split('Email: ')[1].split(' ')[0] + "@cs.nyu.edu"
        else:
            email = None

        if website:
            try:
                new_r = requests.get(website, headers=headers)
                new_soup = BeautifulSoup(new_r.text, 'html.parser')
                research_interests = new_soup.text

                found_keyword = any(re.search(re.escape(keyword), research_interests.lower()) for keyword in keyword_list)

                if found_keyword:
                    pers_link = get_scholar_profile(name)
                    print([u_name, country, name, email, website, pers_link])
                    faculty_data.append([u_name, country, name, email, website, pers_link])

            except requests.exceptions.SSLError as e:
                print(f"SSL error for {website}: {e}")

def nyu():
    urls = ['https://cs.nyu.edu/dynamic/people/faculty/']

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(urls[0], headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('li', class_='col-sm-6')

    print(len(all_profs))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nNew York University done...\n")
    return faculty_data


if __name__ == "__main__":
    nyu()