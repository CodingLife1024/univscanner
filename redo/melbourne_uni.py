import requests
import re
from bs4 import BeautifulSoup
import google_scholar
from requests.exceptions import RequestException, ChunkedEncodingError

u_name = "KAIST"
country = "South Korea"

def kaist():
    url = "https://cis.unimelb.edu.au/people"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    all_categories = soup.find_all('h2', {'class': 'title'})

    for category in all_categories:
        if category.text == "Academic Staff":
            table = category.find_next_sibling('table')
            rows = table.find_all('tr')

                # Iterate through each row
            for row in rows:
                # Extract data from each cell
                name_cell = row.find('td', headers='acad_name')
                surname_cell = row.find('td', headers='acad_surname')
                email_cell = row.find('td', headers='acad_email')

                if name_cell and surname_cell and email_cell:
                    name = name_cell.get_text(strip=True)
                    surname = surname_cell.get_text(strip=True)
                    email = email_cell.find('a').get('href').replace('mailto:', '')

                    # Print name and email (you can modify to store in a list/dict as needed)
                    print(f"Name: {name} {surname}")
                    print(f"Email: {email}")
                    print()

    return faculty_data

# Call the function to extract and print academic staff info
kaist()