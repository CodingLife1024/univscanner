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

u_name = 'McGill University'
country = 'Canada'

def get_faculty_data(prof):
    name_tag = prof.find('h4')
    if name_tag:
        name = name_tag.text.strip()

        research_interests = [p.text.strip() for p in prof.find_all('p', style='margin-left: 15px;')]
        research_interests = " ".join(research_interests)

        found_keyword = any(re.search(re.escape(keyword), research_interests.lower()) for keyword in keyword_list)

        if found_keyword:
            website_tag = prof.find('a', href=True, string='Website')
            if website_tag:
                website = website_tag['href']

            contact_info_tag = prof.find('div', class_='panel-collapse')
            if contact_info_tag:
                contact_info = contact_info_tag.find_all('a', class_='list-group-item')
                if len(contact_info) > 1:
                    email_info = contact_info[1].text.strip()
                    email_match = re.search(r'Email:\s*([^\s]+)', email_info)
                    if email_match:
                        pers_link = get_scholar_profile(name)
                        print([u_name, country, name, email_match.group(1), website, pers_link])
                        faculty_data.append([u_name, country, name, email_match.group(1), website, pers_link])

def mcgill():
    url = 'https://www.cs.mcgill.ca/people/faculty/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_profs = soup.find_all('div', class_='list-group')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nMcGill University done...\n")
    return faculty_data


if __name__ == '__main__':
    mcgill()