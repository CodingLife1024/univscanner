from bs4 import BeautifulSoup
import requests
import re
from unidecode import unidecode

university = "Oxford"
country = "UK"

def normalize_email(email):
    # Replace common variations with '@'
    email = re.sub(r'\s+at\s+', '@', email)
    email = re.sub(r'\s*\(\s*a\s*\)\s*', '@', email)
    email = re.sub(r'\s*\{\s*at\s*\}\s*', '@', email)
    email = re.sub(r'\s*\(dot\)\s*', '.', email)
    email = re.sub(r'\s*\{\s*dot\s*\}\s*', '.', email)
    email = re.sub(r'\s*\[\s*dot\s*\]\s*', '.', email)
    return email

def oxford():
    url = "https://www.cs.ox.ac.uk/people/faculty.html"

    response = requests.get(url)
    html_content = response.text

    keyword_list = ["embedded system", "computer systems", "kernel", "robotics", "operating system", "autonomous system", "human-robot interaction", "coordination", "decision making", "sensor networks"]

    faculty_data = []

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    extract_webpage = soup.find_all('span', itemprop='name')
    for element in extract_webpage:
        name = element.get_text().strip()
        # print("Name:", name)
        href = "https://www.cs.ox.ac.uk/people/" + unidecode(name).lower().replace(" ", ".")
        # print("URL:", href)

        new_resonse = requests.get(href)
        new_content = new_resonse.text

        new_soup = BeautifulSoup(new_content, 'html.parser')

        if any(keyword in new_soup.get_text().lower() for keyword in keyword_list):
            # print("Research:", "Yes")

            try:
                email = new_soup.find('div', class_='scaled-text', itemprop='email').get_text()[3:]
                email = normalize_email(email)
            except AttributeError:
                email = "Email not found"

            faculty_data.append([university, country, name, email, href])
            print([university, country, unidecode(name), email, href])
    return faculty_data

# oxford()