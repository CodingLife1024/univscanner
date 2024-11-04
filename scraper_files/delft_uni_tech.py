import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "Delft University of Technology"
country = "Netherlands"

def get_faculty_data(prof):
    name_element = prof.find("h3")
    if name_element:
        name = re.sub(r'Prof\.dr\.ir\.|Prof\.dr\.', '', name_element.text).strip()
        profile_link = prof.find("a", href=True)["href"] if prof.find("a", href=True) else None

        if profile_link:
            new_r = requests.get(profile_link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            email = new_soup.find('a', class_='i-mail')['href'][7:] if new_soup.find('a', class_='i-mail') else None
            research = new_soup.text

            found_keyword = any(re.search(re.escape(keyword), research.lower()) for keyword in keyword_list)

            if found_keyword:
                pers_link = get_scholar_profile(name)
                print([u_name, name, email, profile_link, pers_link])
                faculty_data.append([u_name, name, email, profile_link, pers_link])

def decode_email(encoded_email):
    """Decode the email address from the HTML character codes"""
    decoded_email = ''.join([chr(int(code)) for code in re.findall(r'&#(\d+);', encoded_email)])
    return decoded_email

def delft_uni_tech():
    url = "https://www.tudelft.nl/en/eemcs/the-faculty/professors"   # homepage url
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all("div", class_="profile theme-blue hoverableBlock hoverableBlock--green hoverableBlock--hasLink")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nDelft University of Technology done...\n")
    return faculty_data


if __name__ == "__main__":
    delft_uni_tech()