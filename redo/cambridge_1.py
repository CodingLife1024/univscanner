from bs4 import BeautifulSoup
import requests
import re

university = "Cambridge"
country = "UK"

def cambridge():
    url_os = "https://www.cst.cam.ac.uk/research/themes/systems-and-networking"
    url_emb = "https://www.cst.cam.ac.uk/research/themes/mobile-systems-robotics-and-automation"
    url_ca = "https://www.cst.cam.ac.uk/research/themes/computer-architecture"

    response_os = requests.get(url_os)
    response_emb = requests.get(url_emb)
    response_ca = requests.get(url_ca)
    html_content = response_os.text + response_emb.text + response_ca.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

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


                print([university, country, name, email, indiv_url])





cambridge()