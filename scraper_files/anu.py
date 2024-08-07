import requests
from bs4 import BeautifulSoup
import re
from components.google_scholar import get_scholar_profile
import concurrent.futures

u_name = "Australian National University"
country = "Australia"

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

def get_faculty_data(faculty):
    name = faculty.find('p', class_='card__title').text.strip()

    title = faculty.find('p', class_='card__subtitle').text.strip() if faculty.find('p', class_='card__subtitle') else "Not Found"

    if "lecturer" in title.lower() or "professor" in title.lower():
        link_tag = faculty.find('a', class_='card__link')
        if link_tag:
            link = "https://comp.anu.edu.au" + link_tag['href']

            # Append faculty data as a dictionary
            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, "html.parser")

            content = new_soup.find('article', class_='detail__page-content').get_text().strip()

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

def anu():
    url = "https://comp.anu.edu.au/people/"

    r = requests.get(url)

    # Getting the soup by parsing the HTML response
    soup = BeautifulSoup(r.text, "html.parser")

    # Find all article elements with the class "card"
    faculty_divs = soup.find_all('article', class_='card')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, faculty) for faculty in faculty_divs]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if result:
                    faculty_data.append(result)
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("ANU done....")
    print()
    return faculty_data

# anu()
