from bs4 import BeautifulSoup
import requests
import re
from unidecode import unidecode

university = "UCL London"
country = "UK"

def ucl_london():
    url = "https://www.ucl.ac.uk/computer-science/people/computer-science-academic-staff"

    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Find all tables containing professor information
    tables = soup.find_all('table')

    # Iterate through each table
    for table in tables:
        # Find all rows in the table body
        rows = table.find_all('tr')
        # Iterate through each row skipping the header row
        for row in rows[1:]:
            # Extract the name, role, email, and URL
            columns = row.find_all('td')
            name = columns[0].text.strip()
            role = columns[1].text.strip()
            email = columns[2].find('a').text.strip()
            url = columns[0].find('a')['href']

            new_soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            research_text = new_soup.text





            found_keyword = any(re.search(re.escape(keyword), (research_text + role).lower()) for keyword in keyword_list)
            if found_keyword:
                print([university, country, unidecode(name), role, email, url])
                faculty_data.append([university, country, unidecode(name), email, url])
    print()
    print("UCL London done...")
    print()
    return faculty_data

# ucl_london()