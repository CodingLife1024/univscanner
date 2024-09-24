import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import unidecode as unidecode

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Northwestern University"
country = "United States"

def get_name(prof):
    name = prof.find('h3').text
    return name

def get_link(prof):
    link = prof.find('a', class_=None)['href'] if prof.find('a', class_=None) else "N/A"
    return link

def get_email(prof):
    email = prof.find('a', class_='mail_link')['href'][7:] if prof.find('a', class_='mail_link') else "N/A"
    return email

def get_faculty_data(prof, headers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_name = executor.submit(get_name, prof)
        future_link = executor.submit(get_link, prof)
        future_email = executor.submit(get_email, prof)

        name = future_name.result()
        link = future_link.result()
        email = future_email.result()

    if link !="N/A":
        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, "html.parser")

        personal_website_h2_element = new_soup.find('h2', class_='sites-header')
        if personal_website_h2_element:
            a_tag = personal_website_h2_element.find_next('a')
            if a_tag:
                personal_link = a_tag.get('href')
            else:
                personal_link = get_scholar_profile(name)
        else:
            personal_link = get_scholar_profile(name)

        research_interests_h2 = new_soup.find('h2', string='Research Interests')
        if research_interests_h2:
            research_interests_p = research_interests_h2.find_next('p')
            if research_interests_p:
                research_interests = research_interests_p.text
                found_keyword = any(re.search(re.escape(keyword), research_interests) for keyword in keyword_list)

                if found_keyword:
                    print([u_name, country, unidecode.unidecode(name), email, link, personal_link])
                    faculty_data.append([u_name, country, unidecode.unidecode(name), email, link, personal_link])


def northwestern():
    url = "https://www.mccormick.northwestern.edu/computer-science/people/faculty/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # Send a GET request to the URL
    r = requests.get(url, headers=headers)

    # Parse the page content
    soup = BeautifulSoup(r.text, "html.parser")

    # Find all div elements with the class "faculty-info"
    all_profs = soup.find_all('div', class_='faculty-info')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Northwestern University done....")
    print()

    return faculty_data

if __name__ == "__main__":
    northwestern()