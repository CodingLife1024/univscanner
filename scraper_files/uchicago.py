from bs4 import BeautifulSoup
import requests
import re

university = "University of Chicago"
country = "USA"

def uchicago():
    url = "https://www.cs.uchicago.edu/people/faculty/"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    # Find all divs with class 'card card--person'
    faculty_cards = soup.find_all('div', class_='card card--person')

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Iterate over each faculty card
    for card in faculty_cards:
        # Find the name of the faculty member (inside h3 tag with class 'card__title')
        name_element = card.find('h3', class_='card__title')
        name = name_element.text.strip() if name_element else "Name not found"
        # print("Name:", name)

        # Find the URL (inside the 'a' tag with class 'card__url')
        url_element = card.find('a', class_='card__url')
        url = url_element['href'] if url_element else "URL not found"
        # print("URL:", url)

        new_response = requests.get(url)
        new_soup = BeautifulSoup(new_response.text, "html.parser")

        # Find the email (inside the 'a' tag with class 'card__email')
        email_element = new_soup.find('div', class_='person-detail__value')
        email = email_element.get_text() if email_element else "Email not found"
        #print("Email:", email.get_text())

        found_keyword = any(re.search(re.escape(keyword), new_response.text) for keyword in keyword_list)

        if found_keyword:
            faculty_data.append([university, country, name, email, url])
            print([university, country, name, email, url])


    print()
    print("University of Chicago done...")
    print()
    return faculty_data

# uchicago()
