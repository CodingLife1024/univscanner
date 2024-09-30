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

u_name = "Dartmouth College"
country = "United States"

def get_name(prof):
    name = prof.find('div', class_="content").find('a').text.strip()
    return name

def get_link(prof):
    link = 'https://web.cs.dartmouth.edu' + prof.find('div', class_="content").find('a')['href']
    return link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)

        name = future_name.result()
        link = future_link.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    email = new_soup.find('a', href=re.compile(r"^mailto:")).text.strip()
    research_stuff = new_soup.find_all('h3', class_="label field-label")

    research = ""

    for i in research_stuff:
        new = i.find_parent('div', class_="pane-content").text
        research += new

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        pers_link = new_soup.find('a', text='Personal Website')['href'] if new_soup.find('a', text='Personal Website') else get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def dartmouth():
    urls = ["https://web.cs.dartmouth.edu/people"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")
    super_class = soup.find_all('ul', class_='people-list clearfix')[:4]

    all_profs = []

    for i in super_class:
        profs = i.find_all('li', class_="")
        all_profs.extend(profs)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Dartmouth College done...")
    print()


if __name__ == '__main__':
    dartmouth()