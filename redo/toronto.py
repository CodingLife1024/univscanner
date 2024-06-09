import requests
from bs4 import BeautifulSoup

university = "University of Toronto"
country = "Canada"

def toronto():
    url = "https://web.cs.toronto.edu/people/faculty-directory"  # homepage URL
    r = requests.get(url)  # request to URL

    # Getting the soup by parsing the HTML parser to text to request r
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    # Find the blueTable table
    blue_table = soup.find('table', class_='blueTable')

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    if blue_table:
        # Find all rows in the table except the header row
        rows = blue_table.find_all('tr')[1:]

        for row in rows:
            columns = row.find_all('td')

            # Extracting name and position
            name_tag = columns[0].find('a')
            name = name_tag.text.strip() if name_tag else 'No name found'
            website = name_tag['href'] if name_tag else 'No website found'

            # Extracting email
            email_tag = columns[1].find('a', href=True)
            email = email_tag['href'].replace('mailto:', '') if email_tag and 'mailto:' in email_tag['href'] else 'No email found'

            # Extracting research areas
            research_areas = columns[2].text.strip() if len(columns) > 2 else 'No research areas found'

            found_keyword = any(keyword in (research_areas).lower() for keyword in keyword_list)

            if found_keyword:
                faculty_data.append([university, country, name, email, website])
                print([university, country, name, email, website])


    print()
    print("University of Toronto done...")
    print()

    return faculty_data

# toronto()