from bs4 import BeautifulSoup
import requests

url = "https://seas.harvard.edu/computer-science/faculty-research"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <div> tags with class 'accordion-content' that are siblings to <a> tags with the specified titles
accordion_titles = ["Robotics and Control", "Theory of Computation"]

for title in accordion_titles:
    accordion_title_element = soup.find('a', class_='accordion-title', string=title)

    if accordion_title_element:
        # Find the next <div> tag with class 'accordion-content' after the accordion title
        accordion_content = accordion_title_element.find_next_sibling('div', class_='accordion-content')

        if accordion_content:
            # Find all <a> tags within the accordion content
            links = accordion_content.find_all('a')
            print(f"Links under '{title}':")
            for link in links:
                print("Name:", link.get_text(strip=True))
                print("URL:", "https://seas.harvard.edu" + link.get('href'))

            print()
        else:
            print(f"No content found under '{title}'.")
    else:
        print(f"Accordion title '{title}' not found.")

