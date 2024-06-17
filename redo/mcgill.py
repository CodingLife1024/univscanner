import re
import requests
from bs4 import BeautifulSoup
import google_scholar

u_name = 'McGill University'
country = 'Canada'

def mcgill():
    url = 'https://www.cs.mcgill.ca/people/faculty/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    faculty_data = []

    profs = soup.find_all('div', class_='list-group')

    for prof in profs:
        name_tag = prof.find('h4')
        if name_tag:
            name = name_tag.text.strip()
            # print(name)

            research_interests = [p.text.strip() for p in prof.find_all('p', style='margin-left: 15px;')]
            research_interests = " ".join(research_interests)
            # print(research_interests)

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
                            # print(email_match.group(1))
                            print([u_name, country, name, email_match.group(1), website, google_scholar.get_scholar_profile(name)])
                            faculty_data.append([u_name, country, name, email_match.group(1), website, google_scholar.get_scholar_profile(name)])

    print()
    print("McGill University done....")
    print()

    return faculty_data

# mcgill()
