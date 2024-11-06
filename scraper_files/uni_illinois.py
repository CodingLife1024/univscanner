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

u_name = "University of Illinois at Urbana-Champaign"
country = "United States"

def get_name(prof):
    return prof.find('div', class_="name").text.strip()

def get_link(prof):
    link = "https://siebelschool.illinois.edu" + prof.find('div', class_="name").find('a').get('href')
    return link

def get_email(prof):
    return prof.find('div', class_="email hide-empty")['data-value']

def get_research(prof, name):
    link = get_link(prof)
    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    pers_link = new_soup.find('h2', string="For More Information").find_next('ul').find('a')['href'] if new_soup.find('h2', string="For More Information") else get_scholar_profile(name)

    research_interests = new_soup.find('h2', string="Research Interests").find_next('ul').text if new_soup.find('h2', string="Research Interests") else ""

    research_areas = new_soup.find('h2', string="Research Areas").find_next('ul').text if new_soup.find('h2', string="Research Areas") else ""

    research = research_interests + research_areas

    return research, pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        # Collect results
        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    research, pers_link = get_research(prof, name)

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        print([u_name, country, name, email, link, pers_link])
        faculty_data.append([u_name, country, name, email, link, pers_link])

def uni_illinois():
    url = "https://cs.illinois.edu/about/people/all-faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_="details")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\n" + u_name +" done..." + "\n")
    return faculty_data


if __name__ == "__main__":
    uni_illinois()