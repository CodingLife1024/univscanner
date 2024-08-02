import requests
from bs4 import BeautifulSoup
import re
from components.google_scholar import get_scholar_profile
import unidecode as unidecode

u_name = "Northwestern University"
country = "USA"

def northwestern():
    url = "https://www.mccormick.northwestern.edu/computer-science/people/faculty/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Send a GET request to the URL
    r = requests.get(url, headers=headers)

    # Parse the page content
    soup = BeautifulSoup(r.text, "html.parser")

    # Find all div elements with the class "faculty-info"
    d = soup.find_all('div', class_='faculty-info')

    faculty_data = []

    for i in d:
        name = i.find('h3').text
        link = i.find('a', class_=None)['href'] if i.find('a', class_=None) else None
        email = i.find('a', class_='mail_link')['href'][7:] if i.find('a', class_='mail_link') else None

        # print(f"Name: {name}\nLink: {link}\nEmail: {email}\n")

        if link:
            new_r = requests.get(link, headers=headers)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            # Correctly refer to new_soup for the personal website link
            personal_website_h2_element = new_soup.find('h2', class_='sites-header')
            if personal_website_h2_element:
                a_tag = personal_website_h2_element.find_next('a')
                if a_tag:
                    personal_link = a_tag.get('href')
                    # print(f"Personal Website: {personal_link}")
                else:
                    personal_link = get_scholar_profile(name)
            else:
                personal_link = get_scholar_profile(name)

            # Extract research interests
            research_interests_h2 = new_soup.find('h2', string='Research Interests')
            if research_interests_h2:
                research_interests_p = research_interests_h2.find_next('p')
                if research_interests_p:
                    research_interests = research_interests_p.text
                    found_keyword = any(re.search(re.escape(keyword), research_interests) for keyword in keyword_list)

                    if found_keyword:
                        print([u_name, country, unidecode.unidecode(name), email, link, personal_link])
                        faculty_data.append([u_name, country, unidecode.unidecode(name), email, link, personal_link])

    print()
    print("Northwestern University done....")
    print()

    return faculty_data

# Call the function
# northwestern()
