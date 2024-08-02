import requests
from bs4 import BeautifulSoup

def melbourne_uni():
    url = "https://cis.unimelb.edu.au/people"

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Finding all categories with the title 'Academic staff'
    all_categories = soup.find_all('h2', {'class': 'title'})

    for category in all_categories:
        if category.text.strip() == "Academic staff":
            table = category.find_next_sibling('table')
            rows = table.find_all('tr')

            for row in rows:
                name_cell = row.find('td', headers='acad_name')
                surname_cell = row.find('td', headers='acad_surname')
                profile_cell = row.find('td', headers='acad_profile')
                email_cell = row.find('td', headers='acad_email')

                if name_cell and surname_cell and email_cell and profile_cell:
                    name = name_cell.get_text(strip=True)
                    surname = surname_cell.get_text(strip=True)
                    profile = profile_cell.find('a').get('href') if profile_cell.find('a') else None
                    email = email_cell.find('a').get('href').replace('mailto:', '')

                    print(name + " " + surname)
                    print(profile)
                    print(email)

                    if profile:
                        new_r = requests.get(profile)
                        new_soup = BeautifulSoup(new_r.text, "html.parser")

                        research_areas = []
                        tags = new_soup.find_all('div', class_='research-area-tag')
                        for tag in tags:
                            research_areas.append(tag.get_text(strip=True))

                        print(f"Research Areas: {', '.join(research_areas)}")
                    print()



# Call the function to extract and print academic staff info
melbourne_uni()
