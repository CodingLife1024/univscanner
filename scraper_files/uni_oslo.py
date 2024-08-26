import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

u_name = "University of Oslo"
country = "Norway"

faculty_data = []

def get_faculty_data(prof):
    columns = prof.find_all('td')
    if len(columns) < 3:
        return
    name_element = columns[0].find('a', string=lambda text: text is not None)
    name = name_element.text.split(",")[1] + " " + name_element.text.split(",")[0] if name_element else "N/A"

    link = name_element['href'] if name_element else "N/A"

    email_element = columns[2].find('a')
    email = email_element.get('href', '')[7:] if email_element else "N/A"

    title = columns[0].text if name_element else "N/A"

    if ("student" in email.lower() or "fellow" in name.lower() or "emeritus" in title.lower()):
        return

    new_r = requests.get(link)
    research = new_r.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword or True:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_oslo():
    urls = ["https://www.mn.uio.no/ifi/english/people/aca/",
            "https://www.mn.uio.no/ifi/english/people/aca/?page=2&u-page=2",
            "https://www.mn.uio.no/ifi/english/people/aca/?page=3&u-page=3",
            "https://www.mn.uio.no/ifi/english/people/aca/?page=4&u-page=4"]

    total_text = ""
    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find('table', class_="vrtx-person-listing").find_all('tr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("University of Oslo done...")
    print()
    return faculty_data


if __name__ == '__main__':
    uni_oslo()