import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
from components.google_scholar import get_scholar_profile

u_name = "Carnegie Mellon University"
country = "United States"

faculty_data = []

def fetch_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def extract_name(professor):
    try:
        last_name = professor.find('td', class_='views-field-field-last-name').find('a').text.strip()
        first_name = professor.find('td', class_='views-field-field-first-name').find('a').text.strip()
        return f"{last_name} {first_name}"
    except AttributeError:
        return None

def extract_email_and_personal_page(new_soup):
    email = "N/A"
    personal_page_link = None

    all_strong_text = new_soup.find_all('p')
    for strong_text in all_strong_text:
        if "Email" in strong_text.text:
            email = strong_text.text[6:].strip()
        elif "Website" in strong_text.text:
            personal_page_link = strong_text.find('a').get('href')

    return email, personal_page_link

def get_faculty_data(professor):
    try:
        name = extract_name(professor)
        if not name:
            return

        link = "https://csd.cmu.edu" + professor.find('a').get('href')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_soup = executor.submit(fetch_soup, link)
            new_soup = future_soup.result()

            future_email_personal = executor.submit(extract_email_and_personal_page, new_soup)
            email, personal_page_link = future_email_personal.result()

        if not personal_page_link:
            personal_page_link = get_scholar_profile(name)

        print([u_name, country, name, email, link, personal_page_link])
        faculty_data.append([u_name, country, name, email, link, personal_page_link])

    except Exception as e:
        print(f"Error occurred: {e}")

def carnegie_mellon():
    urls = [
        "https://csd.cmu.edu/research/research-areas/computer-architecture",
        "https://csd.cmu.edu/research/research-areas/distributed-systems",
        "https://csd.cmu.edu/research/research-areas/operating-systems",
        "https://csd.cmu.edu/research/research-areas/human-computer-interaction",
        "https://csd.cmu.edu/research/research-areas/robotics"
    ]

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        tables = soup.find_all('table', {'class': 'cols-4'})

        for table in tables:
            professors = table.find_all('tr')

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(get_faculty_data, professor) for professor in professors]
                for future in concurrent.futures.as_completed(futures):
                    try:
                        future.result()  # Ensure exceptions are raised
                    except Exception as e:
                        print(f"Error occurred: {e}")

    print("\nCarnegie Mellon done...\n")
    return faculty_data


if __name__ == "__main__":
    carnegie_mellon()
