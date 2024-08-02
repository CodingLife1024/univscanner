import requests
import re
from bs4 import BeautifulSoup
import redo.google_scholar

u_name = "University of California, Berkeley"
country = "USA"

def uc_berkeley():
    url = "https://www2.eecs.berkeley.edu/Faculty/Lists/CS/faculty.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)

    # Getting the soup by parsing the HTML response
    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    faculty_data = []

    # Find all div elements with the class "cc-image-list__item__content"
    faculty_divs = soup.find_all('div', class_='cc-image-list__item__content')

    # Iterate over each faculty member's div
    for faculty in faculty_divs:
        # Extract the name
        name_tag = faculty.find('h3').find('a')
        name = name_tag.text.strip()
        link = 'https://www2.eecs.berkeley.edu' + name_tag['href']

        # Extract the email
        email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", faculty.text)
        email = email_match.group(0) if email_match else "Not Found"

        # Extract research areas
        research_areas_tag = faculty.find('strong', string='Research Interests:')
        research_areas = research_areas_tag.next_sibling.strip() if research_areas_tag else "Not Found"

        # Additional logic to handle multiple research areas
        if research_areas_tag:
            research_areas = []
            for a_tag in research_areas_tag.find_next_siblings('a'):
                research_areas.append(a_tag.text.strip())
            research_areas = '; '.join(research_areas)

        # print(f"Name: {name}")
        # print(f"Email: {email}")
        # print(f"Link: {link}")
        # print(f"Research Areas: {research_areas}")

        found_keyword = any(keyword.lower() in research_areas.lower() for keyword in keyword_list)

        if found_keyword:
            new_r = requests.get(link, headers=headers)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            personal_website_tag = new_soup.find('a', string='Personal Homepage')
            if personal_website_tag:
                personal_website = personal_website_tag.get('href')
            else:
                personal_website = google_scholar.get_scholar_profile(name)

                print([u_name, country, name, email, link, personal_website])
                faculty_data.append([u_name, country, name, email, link, personal_website])

    print()
    print("UC Berkeley done....")
    print()
    return faculty_data

# uc_berkeley()
