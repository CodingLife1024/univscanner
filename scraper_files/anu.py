import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

u_name = "Australian National University"
country = "Australia"

faculty_data = []

def extract_email(new_soup):
    email_links = new_soup.find('a', href=lambda href: href and href.startswith("mailto:"))
    return email_links['href'][7:] if email_links else "N/A"

def extract_website(new_soup, name):
    strong_tag = new_soup.find('strong', string='Website')
    if strong_tag:
        next_a_tag = strong_tag.find_next('a')
        if next_a_tag:
            return next_a_tag['href']
    return get_scholar_profile(name)

def extract_content(new_soup):
    return new_soup.find('article', class_='detail__page-content').get_text().strip()

def get_faculty_data(faculty):
    name = faculty.find('p', class_='card__title').text.strip()
    title = faculty.find('p', class_='card__subtitle').text.strip() if faculty.find('p', class_='card__subtitle') else "Not Found"

    if "lecturer" in title.lower() or "professor" in title.lower():
        link_tag = faculty.find('a', class_='card__link')
        if link_tag:
            link = "https://comp.anu.edu.au" + link_tag['href']
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_email = executor.submit(extract_email, new_soup)
                future_website = executor.submit(extract_website, new_soup, name)
                future_content = executor.submit(extract_content, new_soup)

                email = future_email.result()
                website_link = future_website.result()
                content = future_content.result()

            found_keyword = any(re.search(re.escape(keyword), content, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                print([u_name, country, name, email, link, website_link])
                faculty_data.append([u_name, country, name, email, link, website_link])

def anu():
    url = "https://comp.anu.edu.au/people/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    faculty_divs = soup.find_all('article', class_='card')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, faculty) for faculty in faculty_divs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Ensure exceptions are raised
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nAustralian National University done...\n")
    return faculty_data


if __name__ == "__main__":
    anu()