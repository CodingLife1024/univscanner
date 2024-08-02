from bs4 import BeautifulSoup
import requests
import re

university = "University of Pennsylvania"
country = "USA"

def upenn():
    url = "https://directory.seas.upenn.edu/computer-and-information-science/"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer", "systems engineering", "systems"]

    faculty_data = []

    faculty_cards = soup.find_all(class_=re.compile(r'col-12.*SingleStaffList.*ft-cis'))

    for faculty in faculty_cards:
        # Extracting the information from the parent div
        name = faculty.find('div', class_='StaffListName').text.strip()
        site = faculty.find('a')['href'].strip()
        email_a_tag = faculty.find('a', href=lambda href: href and href.startswith("mailto:"))

        # print("Name:", name)
        # print("Site:", site)

        if email_a_tag:
            email = email_a_tag['href'].replace('mailto:', '')
            # print("Email:", email)

        expertise = faculty.find('div', class_='StaffListTitles').text.strip()
        # print("Expertise:", expertise.strip().replace('\n', ' ').replace('\r', ' '))

        new_r = requests.get(site)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        pers_site = new_soup.find('a', string='Personal Website')['href'] if new_soup.find('a', string='Personal Website') else "Personal Website not found"

        # print("Personal Site:", pers_site)

        if pers_site != "Personal Website not found":
            try:
                pers_r = requests.get(pers_site)
                pers_soup = BeautifulSoup(pers_r.text, 'html.parser')
                pers_text = pers_soup.text
            except:
                continue

        else:
            pers_soup = None
            pers_text = ""

        found_keyword = False

        if pers_soup:
            found_keyword = any(re.search(re.escape(keyword), (pers_text + expertise).lower()) for keyword in keyword_list)

        if found_keyword:

            faculty_data.append([university, country, name, email, site, pers_site])
            print([university, country, name, email, site, pers_site])


    print()
    print("University of Pennsylvania done...")
    print()
    return faculty_data

# upenn()
