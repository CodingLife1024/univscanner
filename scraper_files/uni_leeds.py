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

u_name = "University of Leeds"
country = "United Kingdom"

def get_name(prof):
    last_name_tag = prof.find('td', {'class': 'title'}).find('a')
    if last_name_tag:
        first_name = last_name_tag.find_next('td').get_text().strip()
        full_name = f"{first_name} {last_name_tag.get_text().strip()}"
        return full_name

def get_link(prof):
    last_name_tag = prof.find('td', {'class': 'title'}).find('a')
    if last_name_tag:
        link = last_name_tag['href']
        return link

def get_email(prof):
    email_tag = prof.find('a', href=re.compile(r'mailto:'))
    email = email_tag.get_text().strip() if email_tag else "N/A"
    return email

def get_research(new_soup):
    research = new_soup.find('ul', {'class': 'list-facts'}).get_text().strip()
    return research

def get_personal_link(new_soup, full_name):
    pers_link = new_soup.find('a', string="Personal Website")['href'] if new_soup.find('a', string="Personal Website") else get_scholar_profile(full_name)
    return pers_link

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        full_name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_research = executor.submit(get_research, new_soup)
        future_pers_link = executor.submit(get_personal_link, new_soup, full_name)

        research = future_research.result()
        pers_link = future_pers_link.result()

    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)
    if found_keyword:
        faculty_data.append([u_name, country, full_name, email, link, pers_link])
        print([u_name, country, full_name, email, link, pers_link])


def uni_leeds():
    urls = [
        "https://eps.leeds.ac.uk/computing/stafflist?categorySlug=computing&page=1",
        "https://eps.leeds.ac.uk/computing/stafflist?categorySlug=computing&page=2",
        "https://eps.leeds.ac.uk/computing/stafflist?categorySlug=computing&page=3",
        "https://eps.leeds.ac.uk/computing/stafflist?categorySlug=computing&page=4",
        "https://eps.leeds.ac.uk/computing/stafflist?categorySlug=computing&page=5",
        "https://eps.leeds.ac.uk/computing/stafflist?categorySlug=computing&page=6",
    ]

    all_profs = []

    # Loop over each URL and process separately
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all the professor rows in the current page
        profs_on_page = soup.find('table', {'class': 'tablesaw table-profiles table-hover'}).find('tbody').find_all('tr')
        all_profs.extend(profs_on_page)  # Combine all the professors from different pages

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Leeds done...\n")
    return faculty_data


if __name__ == "__main__":
    uni_leeds()