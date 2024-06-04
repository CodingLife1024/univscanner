from bs4 import BeautifulSoup
import requests
import re

def upenn():
    url = "https://directory.seas.upenn.edu/computer-and-information-science/"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    facultydata = []

    faculty_cards = soup.find_all(class_=re.compile(r'col-12.*SingleStaffList.*ft-cis'))

    for faculty in faculty_cards:
        # Extracting the information from the parent div
        name = faculty.find('div', class_='StaffListName').text.strip()
        site = faculty.find('a')['href'].strip()
        email_a_tag = faculty.find('a', href=lambda href: href and href.startswith("mailto:"))

        print("Name:", name)
        print("Site:", site)

        if email_a_tag:
            email = email_a_tag['href'].replace('mailto:', '')
            print("Email:", email)

        new_r = requests.get(site)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        print()

upenn()
