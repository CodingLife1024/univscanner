import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

university = "Korea University"
country = "South Korea"


def get_faculty_data(prof):
    name_tag = prof.find('dt')
    email_tag = name_tag.find_next('dd')
    link_tag = email_tag.find_next('dd') if email_tag else None
    research_tag = link_tag.find_next('dd') if link_tag else None

    if name_tag and email_tag:
        name = name_tag.text.strip()
        email = email_tag.text.strip()

        found_keyword = any(re.search(re.escape(keyword), research_tag.text.strip().lower()) for keyword in keyword_list)

        if link_tag and found_keyword:
            link = link_tag.text.strip()

            # Concurrently fetch scholar profile
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(get_scholar_profile, name)
                scholar_profile = future.result()

            faculty_data.append([university, country, name, email, link, scholar_profile])
            print([university, country, name, email, link, scholar_profile])
    else:
        print("Missing required tags (name or email).")

def korea_uni():
    url = "https://cs.korea.edu/en_cs/intro/fulltime_faculty.do?mode=list&&articleLimit=100&article.offset=0"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    all_profs = soup.find('div', class_='pro_list').find_all('div', class_="", recursive=False)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Ensure exceptions are raised
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nKorea University done...\n")
    return faculty_data

if __name__ == "__main__":
    korea_uni()