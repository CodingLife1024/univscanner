from bs4 import BeautifulSoup
import requests
import re

university = "Caltech"
country = "USA"

def caltech():
    url_1 = "https://www.eas.caltech.edu/people/faculty"
    url_2 = "https://www.cms.caltech.edu/people/faculty"

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)
    html_content = response_1.text + response_2.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    # Find all divs with class 'card card--person'
    faculty_cards = soup.find_all('li', class_='person-list__names-only__person')

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Iterate over each faculty card
    for card in faculty_cards:
        # name_element = card.find('a', class_='card__title')
        name = card.get_text().strip() if card else "Name not found"
        # print("Name:", name)

        # # Find the URL (inside the 'a' tag with class 'card__url')
        url_element = card.find('a')
        url = "https://www.cms.caltech.edu" + url_element['href'] if url_element else "URL not found"
        # print("URL:", url)

        email = url[35:] + "@caltech.edu" if url else "Email not found"
        # print("Email:", email)

        new_response = requests.get(url)
        new_soup = BeautifulSoup(new_response.text, "html.parser")

        pers_soup = new_soup.find_all('div', class_='field__personal_url person-page2__link--quicklinks')
        if pers_soup:
            for div in pers_soup:
                pers_url = div.find('a')['href']
                # print("Personal URL:", pers_url)
                # print()
        else:
            pers_url = "Personal URL Not found"
            # print("Personal URL:", url)
            # print()

        text_soup = new_soup.find_all('div', class_='person-page2__field field__research_summary') + new_soup.find_all('div', class_='person-page2__profile-block__profile profile-text')

        # Combine all the text from text_soup into one string
        combined_text = ' '.join(soup.get_text(separator=' ') for soup in text_soup)

        # Check if any of the keywords are found in the combined text
        if any(re.search(re.escape(keyword), combined_text) for keyword in keyword_list):
            faculty_data.append([university, country, name, email, url, pers_url])
            print([university, country, name, email, url, pers_url])

    print()
    print("Caltech done...")
    print()
    return faculty_data

# caltech()

if __name__ == "__main__":
    caltech()