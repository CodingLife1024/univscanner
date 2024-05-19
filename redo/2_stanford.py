from bs4 import BeautifulSoup
import requests
import re

university = "Stanford"
country = "USA"

def stanford():
    url_os = "https://www.cs.stanford.edu/people-cs/faculty-research/operatingdistributed-systems"
    url_emb = "https://www.cs.stanford.edu/people-cs/faculty-research/robotics"

    response_os = requests.get(url_os)
    response_emb = requests.get(url_emb)
    html_content = response_os.text + response_emb.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    extract_webpage = soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('/people/'))

    for element in extract_webpage:
        text_content = element.get_text().strip()  # Separate text content by newlines for better readability
        href = element.get('href')  # Get the href attribute value
        # print("Text Content:", text_content)
        # print("Href:", href)
        indiv_url = "https://www.cs.stanford.edu" + href
        # print("Individual URL:", indiv_url)
        new_response = requests.get(indiv_url)
        new_html_content = new_response.text
        new_soup = BeautifulSoup(new_html_content, 'html.parser')
        extract_email = new_soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('mailto:'))
        if not extract_email:
            email = "Email Not Provided"
        else:
            email = extract_email[0].get_text()
        # print("Email:", email)
        print([university, country, text_content, email, indiv_url])

    print("Stanford Done....")

if __name__ == "__main__":
    stanford()