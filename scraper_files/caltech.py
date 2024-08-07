from bs4 import BeautifulSoup
import requests
import re
from components.google_scholar import get_scholar_profile
import concurrent.futures

university = "Caltech"
country = "USA"

keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

faculty_data = []

def extract_personal_url(soup, name):
    pers_soup = soup.find_all('div', class_='field__personal_url person-page2__link--quicklinks')
    if pers_soup:
        return pers_soup[0].find('a')['href']
    return get_scholar_profile(name)

def extract_research_summary(soup):
    text_soup = soup.find_all('div', class_='person-page2__field field__research_summary') + soup.find_all('div', class_='person-page2__profile-block__profile profile-text')
    return ' '.join(div.get_text(separator=' ') for div in text_soup)

def get_faculty_data(card):
    name = card.get_text().strip() if card else "Name not found"
    url_element = card.find('a')
    url = "https://www.cms.caltech.edu" + url_element['href'] if url_element else "URL not found"
    email = url[35:] + "@caltech.edu" if url else "Email not found"

    try:
        new_response = requests.get(url)
        new_soup = BeautifulSoup(new_response.text, "html.parser")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_pers_url = executor.submit(extract_personal_url, new_soup, name)
            future_research_summary = executor.submit(extract_research_summary, new_soup)

            pers_url = future_pers_url.result()
            combined_text = future_research_summary.result()

            found_keyword = any(re.search(re.escape(keyword), combined_text.lower()) for keyword in keyword_list)

            if found_keyword:
                faculty_data.append([university, country, name, email, url, pers_url])
                print([university, country, name, email, url, pers_url])
    except Exception as e:
        print(f"Error occurred while processing {name}: {e}")

def caltech():
    url_1 = "https://www.eas.caltech.edu/people/faculty"
    url_2 = "https://www.cms.caltech.edu/people/faculty"

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)
    html_content = response_1.text + response_2.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_cards = soup.find_all('li', class_='person-list__names-only__person')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, card) for card in faculty_cards]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Ensure exceptions are raised
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("Caltech done...")
    print()
    return faculty_data

# Uncomment the following line to run the script
# caltech()
