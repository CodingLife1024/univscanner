from bs4 import BeautifulSoup
import requests
import concurrent.futures
import base64
import re
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

university = "National Taiwan University"
country = "Taiwan"

faculty_data = []

def get_faculty_data(name, base_url="https://csie.ntu.edu.tw", headers=""):
    url = "https://csie.ntu.edu.tw/en/member/Faculty"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    try:
        prof_url = base_url + soup.find('a', string=name + " ").get('href')
    except AttributeError:
        print(f"Profile URL for {name} not found.")
        return None

    # Fetch the individual faculty member's page
    new_response = requests.get(prof_url)
    new_html_content = new_response.text
    new_soup = BeautifulSoup(new_html_content, 'html.parser')

    # Extract email
    script_tag = new_soup.find('td', class_='member-data-value-email').find('script', class_='e-enc')
    if script_tag:
        script_content = script_tag.get_text(strip=True)
        start = script_content.find('atob("') + 6
        end = script_content.find('")', start)
        encoded_email = script_content[start:end]
        email = base64.b64decode(encoded_email).decode('utf-8')
    else:
        email = 'N/A'

    # Extract personal webpage link
    personal_page_tag = new_soup.find('td', class_='member-data-value-6').find('a') if new_soup.find('td', class_='member-data-value-6') else None
    personal_page = personal_page_tag.get('href') if personal_page_tag else get_scholar_profile(name)

    # Extract research expertise
    research_areas_tag = new_soup.find('td', class_='member-data-value-7')
    research_areas = research_areas_tag.get_text(strip=True) if research_areas_tag else 'N/A'

    found_keyword = any(re.search(re.escape(keyword), research_areas.lower()) for keyword in keyword_list)
    if found_keyword:
        print([university, country, name, email, prof_url, personal_page])
        faculty_data.append([university, country, name, email, prof_url, personal_page])

def national_taiwan_university():
    url = "https://csie.ntu.edu.tw/en/member/Faculty"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    member_profile_items = soup.find_all('li', class_='i-member-profile-item')

    names = []
    for item in member_profile_items:
        # Find the span with class 'member-data-title-name'
        title_tag = item.find('span', class_='i-member-title')
        if title_tag and 'Name:' in title_tag.get_text(strip=True):
            # Find the span with class 'member-data-value-name'
            value_tag = item.find('span', class_='member-data-value-name')
            if value_tag:
                a_tag = value_tag.find('a')
                if a_tag:
                    names.append(a_tag.get_text(strip=True))

    base_url = "https://csie.ntu.edu.tw"
    headers= ""

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, name, base_url, headers) for name in names]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("National Taiwan University done...")
    print()
    return faculty_data


if __name__ == "__main__":
    national_taiwan_university()