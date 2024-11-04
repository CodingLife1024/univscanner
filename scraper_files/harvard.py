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

university = "Harvard University"
country = "United States"

def get_faculty_data(title, soup):
    department_element = soup.find('a', class_='accordion-title', string=title)
    if department_element:
        # Find the next <div> tag with class 'accordion-content' after the accordion title
        department_content = department_element.find_next_sibling('div', class_='accordion-content')

        if department_content:
            # Find all <a> tags within the accordion content
            links = department_content.find_all('a')

            for link in links:
                name = link.get_text(strip=True)
                href = "https://seas.harvard.edu" + link.get('href')

                try:
                    new_response = requests.get(href)
                    new_response.raise_for_status()

                    new_content = new_response.text
                    new_soup = BeautifulSoup(new_content, 'html.parser')

                    email = new_soup.find('a', class_=None, id=None, href=lambda href: href and href.startswith('mailto:')).get_text()

                    pers_link = get_scholar_profile(name)

                    if [university, country, name, email, href, pers_link] not in faculty_data:
                        faculty_data.append([university, country, name, email, href, pers_link])
                        print([university, country, name, email, href, pers_link])

                except (requests.exceptions.RequestException, AttributeError) as e:
                    print(f"Error processing {name}:", str(e))
                    continue

def harvard():
    url = "https://www.seas.harvard.edu/computer-science/faculty-research"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        departments = ["Robotics and Control", "Systems, Networks, and Databases"]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(get_faculty_data, title, soup) for title in departments]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error occurred: {e}")

        print("\nHarvard University done...\n")
        return faculty_data

    except requests.exceptions.RequestException as e:
        print("Error fetching Harvard faculty page:", str(e))
        return []

if __name__ == '__main__':
    harvard()