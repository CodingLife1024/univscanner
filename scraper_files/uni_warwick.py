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

u_name = "University of Warwick"
country = "United Kingdom"

def get_faculty_data(prof, headers):
    name = prof.find('h2').text.strip()

    title = prof.find('p').text.strip() if prof.find('p') else "Not Found"

    if "lecturer" in title.lower() or "professor" in title.lower():
        link_tag = prof.find('a')
        if link_tag:
            link = "https://warwick.ac.uk/" + link_tag['href'] if link_tag['href'].startswith("/fac") else link_tag['href']

            try:
                new_r = requests.get(link, headers=headers, verify=True)
                new_r.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Request failed for {link}: {e}")
                return

            new_soup = BeautifulSoup(new_r.text, "html.parser")

            content = new_r.text

            found_keyword = any(re.search(re.escape(keyword), content, re.IGNORECASE) for keyword in keyword_list)

            if found_keyword:
                email_links = new_soup.find('a', href=lambda href: href and href.startswith("mailto:"))
                if email_links:
                    email = email_links['href'][7:]
                else:
                    email = "Email not found"

                strong_tag = new_soup.find('strong', string='Website')

                if strong_tag:
                    next_a_tag = strong_tag.find_next('a')
                    if next_a_tag:
                        website_link = next_a_tag['href']
                    else:
                        website_link = get_scholar_profile(name)
                else:
                    website_link = get_scholar_profile(name)

                print([u_name, country, name, email, link, website_link])
                faculty_data.append([u_name, country, name, email, link, website_link])

def uni_warwick():
    url = "https://warwick.ac.uk/fac/sci/dcs/people/summaries/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    try:
        r = requests.get(url, headers=headers, verify=True)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        raise SystemExit(e)

    soup = BeautifulSoup(r.text, "html.parser")

    all_profs = soup.find_all('div', class_='entryContent')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof, headers) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")


    print("\nUniversity of Warwick done...\n")
    return faculty_data

if __name__ == '__main__':
    uni_warwick()