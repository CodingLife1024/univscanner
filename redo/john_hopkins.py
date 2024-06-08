import requests
from bs4 import BeautifulSoup
import re

university = "John Hopkins University"
country = "USA"

def john_hopkins():
    url = "https://www.cs.jhu.edu/faculty/"   # homepage URL
    r = requests.get(url)                     # request to URL

    # Getting the soup by parsing the HTML parser to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Find all faculty members
    faculty_members = soup.find_all('div', class_='entity')

    for member in faculty_members:
        name_tag = member.find('h2', class_='entity_name')
        email_tag = member.find('a', class_='entity_detail_link')
        link_tag = name_tag.find('a')

        if name_tag and email_tag and link_tag:
            name = name_tag.get_text(strip=True)
            email = email_tag.get_text(strip=True)
            link = link_tag['href']

            # print([name, email, link])

            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            pers_website = new_soup.find_all('a', class_="entity_meta_social_link")

            pers_url = "Personal URL Not Found"

            for website in pers_website:
                if "Website" in website.get('aria-label'):
                    pers_url = website['href']
                    break

            research_sum = new_soup.find('div', class_='page_content').text

            research_labels = new_soup.find_all('div', class_='entity_meta_detail_label', string="Research Areas")

            for label in research_labels:
                # Find the parent div of the current label
                parent_div = label.find_parent('div', class_='entity_meta_detail')

                # Find all subsequent sibling divs with class 'entity_meta_detail_item'
                research_items = parent_div.find_all('div', class_='entity_meta_detail_item')

                # Extract and print the text of each research item
                for item in research_items:
                    research_text = item.get_text(strip=True)
                    research_sum += research_text + " "

                # Check if any of the keywords is present in the professor's webpa
                found_keyword = any(re.search(re.escape(keyword), research_sum) for keyword in keyword_list)
                if found_keyword:
                    faculty_data.append([university, country, name, email, link, pers_url])
                    print([university, country, name, email, link, pers_url])


    print()
    print("John Hopkins University done...")
    print()
    return faculty_data

# john_hopkins()