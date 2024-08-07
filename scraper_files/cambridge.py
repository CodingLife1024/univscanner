from bs4 import BeautifulSoup
import requests
import re
import concurrent.futures
from components.google_scholar import get_scholar_profile

university = "Cambridge"
country = "UK"

faculty_data = []

departments = ["Systems and Networking", "Mobile Systems, Robotics and Automation"]

def extract_department_info(soup):
    depts = soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('https://www.cst.cam.ac.uk/research/themes'))
    return [dept.text.strip() for dept in depts]

def get_personal_url(name):
    return get_scholar_profile(name)

def get_faculty_data(element):
    name = element.get_text().strip()
    if name != "":
        href = element.get('href')  # Get the href attribute value
        if not re.match(r'^/people/directory', href):  # Check if href does not start with '/people/'
            indiv_url = "https://www.cst.cam.ac.uk" + href
            email = indiv_url[33:] + "@cam.ac.uk"

            try:
                new_response = requests.get(indiv_url)
                new_html_content = new_response.text
                new_soup = BeautifulSoup(new_html_content, 'html.parser')

                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future_dept_info = executor.submit(extract_department_info, new_soup)
                    future_personal_url = executor.submit(get_personal_url, name)

                    dept_texts = future_dept_info.result()
                    personal_url = future_personal_url.result()

                    has_intersections = any(dept_text in set(departments) for dept_text in dept_texts)
                    if has_intersections:
                        faculty_data.append([university, country, name, email, indiv_url, personal_url])
                        print([university, country, name, email, indiv_url, personal_url])
            except Exception as e:
                print(f"Error occurred while processing {name}: {e}")

def cambridge():
    url = "https://www.cst.cam.ac.uk//people/directory/faculty"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    extract_webpage = soup.find_all(class_=None, id=None, href=lambda href: href and href.startswith('/people/'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, element) for element in extract_webpage]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Ensure exceptions are raised
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Cambridge done....")
    print()
    return faculty_data

# Uncomment the following line to run the script
# cambridge()
