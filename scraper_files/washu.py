import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

u_name = "Washington University in St. Louis"
country = "United States"

def get_name(prof):
    name = prof.find('h3').text
    return name

def get_link(prof):
    link = prof.find('a')['href']
    return link

def get_title(prof):
    title = prof.find('p', class_="faculty-directory__teaser-title").text
    return title

def get_research(new_soup):
    education = new_soup.find('div', class_="faculty-single__education").text if new_soup.find('div', class_="faculty-single__education") else "N/A"
    research_areas = new_soup.find('div', class_="faculty-single__researchareas").text if new_soup.find('div', class_="faculty-single__researchareas") else "N/A"
    expertise = new_soup.find('div', class_="faculty-single__expertise").text if new_soup.find('div', class_="faculty-single__expertise") else "N/A"
    research = education + research_areas + expertise
    return research

def get_email(new_soup):
    email = new_soup.find('a', href=lambda href: href and href.startswith("mailto:"))['href'][7:] if new_soup.find('a', href=lambda href: href and href.startswith("mailto:")) else "N/A"
    return email

def get_pers_link(new_soup):
    pers_link = new_soup.find('ul', class_="faculty-links").find('li').find_next('li').find('a')['href'] if new_soup.find('ul', class_="faculty-links").find('li').find_next('li').find('a') else "N/A"
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_title = executor.submit(get_title, prof)

        # Collect the results as they complete
        name = future_name.result()
        link = future_link.result()
        title = future_title.result()

    if "Emeritus" not in title:
        new_r = requests.get(link)
        new_content = new_r.text
        new_soup = BeautifulSoup(new_content, 'html.parser')

        with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
            future_email = executor.submit(get_email, new_soup)
            future_research = executor.submit(get_research, new_soup)
            future_pers_link = executor.submit(get_pers_link, new_soup)

            # Collect the results as they complete
            pers_link = future_pers_link.result()
            research = future_research.result()
            email = future_email.result()

        found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([u_name, country, name, email, link, pers_link])
            print([u_name, country, name, email, link, pers_link])


def washu():
    url = "https://cse.washu.edu/faculty-research/directory.html"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find_all('article', class_="faculty-directory__teaser")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Washington University in St. Louis done...")
    print()
    return faculty_data


if __name__ == "__main__":
    washu()