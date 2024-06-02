from bs4 import BeautifulSoup
import requests
import re

university = "MIT"
country = "USA"

def mit():
    url = "https://www.eecs.mit.edu/role/faculty/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    html_content = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags with Name: a, Class: None, ID: None, and 'rel': ['bookmark']
    extract_webpage = soup.find_all('a', class_=None, id=None, rel=['bookmark'])

    departments = ["Robotics", "AI and Society"]

    faculty_data = []

    for element in extract_webpage:
        text_content = element.get_text()  # Separate text content by newlines for better readability
        href = element.get('href')  # Get the href attribute value
        # print("Text Content:", text_content)
        # print("Href:", href)
        indiv_url = href
        new_response = requests.get(indiv_url, headers=headers)
        new_html_content = new_response.text
        new_soup = BeautifulSoup(new_html_content, 'html.parser')
        extract_email = new_soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('mailto:'))
        email = extract_email[0].get_text()
        # print("Email:", email)
        extract_research = new_soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('/people/?fwp_research'))
        # Print all matches as a list
        research_list = [link.get_text() for link in extract_research]
        # print("Research List:", research_list)
        for department in departments:
            if department in research_list:
                print([university, country, text_content, email, href])
                faculty_data.append([university, country, text_content, email, href])


    print()
    print("MIT Done....")
    print()
    return faculty_data

# if __name__ == "__main__":
#     mit()