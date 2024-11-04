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
university = "John Hopkins University"
country = "United States"

def get_name(prof):
    name_tag = prof.find('h2', class_='entity_name')
    name = name_tag.get_text(strip=True)
    return name

def get_email(prof):
    email_tag = prof.find('a', class_='entity_detail_link')
    email = email_tag.get_text(strip=True)
    return email

def get_link(prof):
    name_tag = prof.find('h2', class_='entity_name')
    link_tag = name_tag.find('a')
    link = link_tag['href']
    return link


def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    pers_website = new_soup.find_all('a', class_="entity_meta_social_link")

    pers_url = get_scholar_profile(name)

    for website in pers_website:
        if "Website" in website.get('aria-label'):
            pers_url = website['href']
            break

    research_sum = new_soup.find('div', class_='page_content').text

    research_labels = new_soup.find_all('div', class_='entity_meta_detail_label', string="Research Areas")

    for label in research_labels:
        parent_div = label.find_parent('div', class_='entity_meta_detail')
        research_items = parent_div.find_all('div', class_='entity_meta_detail_item')
        for item in research_items:
            research_text = item.get_text(strip=True)
            research_sum += research_text + " "

        found_keyword = any(re.search(re.escape(keyword), research_sum) for keyword in keyword_list)
        if found_keyword:
            faculty_data.append([university, country, name, email, link, pers_url])
            print([university, country, name, email, link, pers_url])


def john_hopkins():
    url = "https://www.cs.jhu.edu/faculty/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='entity')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nJohn Hopkins University done...\n")
    return faculty_data

if __name__ == "__main__":
    john_hopkins()