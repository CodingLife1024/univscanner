import requests
from bs4 import BeautifulSoup
import re
import google_scholar

u_name = "Carnegie Mellon University"
country = "USA"

def carnegie_mellon():
    urls = [
        "https://csd.cmu.edu/research/research-areas/computer-architecture",
        "https://csd.cmu.edu/research/research-areas/distributed-systems",
        "https://csd.cmu.edu/research/research-areas/operating-systems",
        "https://csd.cmu.edu/research/research-areas/human-computer-interaction",
        "https://csd.cmu.edu/research/research-areas/robotics"
    ]

    faculty_data = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        tables = soup.find_all('table', {'class': 'cols-4'})

        for table in tables:
            professors = table.find_all('tr')

            for professor in professors:
                try:
                    name = professor.find('td', class_='views-field-field-last-name').find('a').text.strip() + " " + professor.find('td', class_='views-field-field-first-name').find('a').text.strip()
                    link = "https://csd.cmu.edu" + professor.find('a').get('href')

                    new_r = requests.get(link)
                    new_soup = BeautifulSoup(new_r.text, "html.parser")

                    all_strong_text = new_soup.find_all('p')

                    personal_page_link = google_scholar.get_scholar_profile(name)
                    email = "Email not found"

                    for strong_text in all_strong_text:
                        if "Email" in strong_text.text:
                            email = strong_text.text[6:].strip()
                            # print(email)
                        elif "Website" in strong_text.text:
                            personal_page_link = strong_text.find('a').get('href')
                            # print(personal_page_link)

                    print([u_name, country, name, email, link, personal_page_link])
                    faculty_data.append([u_name, country, name, email, link, personal_page_link])

                except AttributeError:
                    pass

    print()
    print("Carnegie Mellon done....")
    print()
    return faculty_data

# carnegie_mellon()
