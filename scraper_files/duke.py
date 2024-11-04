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

u_name = "Duke University"
country = "United States"

def get_name(prof):
    name_div = prof.find('div', class_='h4')
    if name_div:
        name = name_div.text.strip()
        profile_link = name_div.find('a')['href'] if name_div.find('a') else None
    return name, profile_link

def get_email(prof):
    email_div = prof.find('div', class_="views-field-field-email")
    email = email_div.text.strip() if email_div else "None"
    if email == "":
        email = "None"
    return email

def get_personal_page(prof, name):
    personal_page = "None"
    websites_field = prof.find('div', class_='views-field-field-websites')
    if websites_field:
        field_content = websites_field.find('div', class_='field-content')
        if field_content:
            link = field_content.find('a')
            if link:
                personal_page = link.get('href', "None")
    if personal_page == "" or personal_page == "None":
        personal_page = get_scholar_profile(name)
    return personal_page

def get_faculty_data(prof):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks for each component
        future_name = executor.submit(get_name, prof)
        future_email = executor.submit(get_email, prof)

        # Collect the results as they complete
        name, profile_link = future_name.result()
        email = future_email.result()

    personal_page = get_personal_page(prof, name)

    if profile_link:
        new_r = requests.get(profile_link)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        overview = new_soup.find('div', class_='excerpt').text if new_soup.find('div', class_='excerpt') else new_r.text

        found_keyword = any(re.search(re.escape(keyword), overview.lower()) for keyword in keyword_list)

        if found_keyword:
            print([u_name, country, name, email, profile_link, personal_page])
            faculty_data.append([u_name, country, name, email, profile_link, personal_page])

def duke():
    url = "https://www.cs.duke.edu/people/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', {'class': 'grid__content'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nDuke University done...\n")
    return faculty_data

if __name__ == '__main__':
    duke()