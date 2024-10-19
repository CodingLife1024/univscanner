import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint
import base64

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "University of Antwerp"
country = "Belgium"

def decode_email(encoded_str):
    try:
        encoded_str = encoded_str.replace(" ", "+")
        encoded_str = encoded_str.encode('utf-8')
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return "N/A"

def get_faculty_data(prof):
    name = prof.find('h3').text.strip()
    link = "https://www.uantwerpen.be" + prof.find('a').get('href')
    email_section = prof.find('div', class_='action actEmail ghost iconRight')
    email = "N/A"

    if email_section:
        encoded_email = email_section.get('data-decode')
        if encoded_email:
            email = decode_email(encoded_email.split(":")[1])

    new_r = requests.get(link)
    new_soup = BeautifulSoup(new_r.text, "html.parser")

    research = new_soup.text
    found_keyword = any(re.search(re.escape(keyword), research, re.IGNORECASE) for keyword in keyword_list)

    if found_keyword:
        pers_link = get_scholar_profile(name)
        faculty_data.append([u_name, country, name, email, link, pers_link])
        print([u_name, country, name, email, link, pers_link])

def uni_antwerp():
    urls = ["https://www.uantwerpen.be/nl/personeel/?q=UA324"]

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    all_profs = soup.find_all('article', {'class': 'wrap'})

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Antwerp done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_antwerp()