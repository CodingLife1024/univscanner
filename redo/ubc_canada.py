import requests
from bs4 import BeautifulSoup
import re
import redo.google_scholar

u_name = "University of British Columbia"
country = "Canada"

def ubc_canada():
    url = "https://www.cs.ubc.ca/people/faculty"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    dd = soup.find('div', {'class': "view-content"})
    d = dd.find_all('tr')

    for row in d:
        # Extract name and link
        name_td = row.find('td', {'headers': "view-field-person-lname-table-column"})
        if not name_td:
            continue  # Skip if the expected td is not found
        a = name_td.find('a', class_="contact-content-name")
        name = (a.get_text()).strip()
        link = 'https://www.cs.ubc.ca' + a.get('href')

        # Extract personal page link if present
        personal_page_a = name_td.find_all('a')[1] if len(name_td.find_all('a')) > 1 else None
        personal_page_link = personal_page_a.get('href') if personal_page_a else google_scholar.get_scholar_profile(name)

        # Extract email
        email_td = row.find('td', {'class': 'views-field-field-person-email'})
        email_a = email_td.find('a', href=re.compile(r'^mailto:')) if email_td else None
        email = email_a.text if email_a else "Email not found"

        # Extract research areas
        research_td = row.find('td', {'headers': "view-field-research-groups-table-column"})
        research_areas = research_td.get_text(strip=True) if research_td else "Research areas not found"

        found_keyword = any(re.search(keyword, research_areas.lower(), re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            print([u_name, country, name, email, link, personal_page_link])
            faculty_data.append([u_name, country, name, email, link, personal_page_link])

    print()
    print("UBC done....")
    print()
    return faculty_data

# ubc_canada()
