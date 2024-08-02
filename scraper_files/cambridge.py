from bs4 import BeautifulSoup
import requests
import re

university = "Cambridge"
country = "UK"

def cambridge():
    url = "https://www.cst.cam.ac.uk//people/directory/faculty"

    response = requests.get(url)
    html_content =response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    departments = ["Systems and Networking", "Mobile Systems, Robotics and Automation"]

    extract_webpage = soup.find_all(class_=None, id=None, href=lambda href: href and href.startswith('/people/'))

    for element in extract_webpage:
        name = element.get_text().strip()
        if name != "":
            href = element.get('href')  # Get the href attribute value
            if not re.match(r'^/people/directory', href):  # Check if href does not start with '/people/'
                # print("Name:", name)
                indiv_url = "https://www.cst.cam.ac.uk" + href
                # print("URL:", indiv_url)
                email = indiv_url[33:] + "@cam.ac.uk"
                # print("Email:", email)
                # print()

                new_response = requests.get(indiv_url)
                new_html_content = new_response.text

                new_soup = BeautifulSoup(new_html_content, 'html.parser')

                depts = new_soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('https://www.cst.cam.ac.uk/research/themes'))

                dept_texts = [dept.text.strip() for dept in depts]

                has_intersections = any(dept_text in set(departments) for dept_text in dept_texts)
                if has_intersections:
                    faculty_data.append([university, country, name, email, indiv_url])
                    print([university, country, name, email, indiv_url])
    print()
    print("Cambridge done....")
    print()
    return faculty_data