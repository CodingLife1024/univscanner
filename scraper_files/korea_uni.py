from bs4 import BeautifulSoup
import requests
import re
import concurrent.futures
from components.google_scholar import get_scholar_profile

university = "Korea University"
country = "South Korea"

faculty_data = []

def korea_uni():
    url = "https://cs.korea.edu/en_cs/intro/fulltime_faculty.do?mode=list&&articleLimit=100&article.offset=0"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_proffs = soup.find('div', class_='pro_list').find_all('div')

    for prof in all_proffs:
        name_tag = prof.find('dt')
        print(name_tag.text)
        email_tag = prof.find('dd')
        print(email_tag.text)

        if name_tag and email_tag:
            name = name_tag.text.strip()
            email = email_tag.text.strip()

            # Ensure email_tag is found before calling find_next()
            link_tag = email_tag.find_next('dd') if email_tag else None

            if link_tag:
                link = link_tag.text.strip()

                try:
                    prof_response = requests.get(link)
                    prof_response.raise_for_status()  # Check if the link is accessible
                except requests.RequestException as e:
                    print(f"Failed to fetch professor's personal page: {e}")
                    continue

                scholar_profile = get_scholar_profile(name)
                faculty_data.append([university, country, name, email, link, scholar_profile])
                print([university, country, name, email, link, scholar_profile])
            else:
                print(f"Link tag not found for professor {name}.")
        else:
            print("Missing required tags (name or email).")

    return faculty_data