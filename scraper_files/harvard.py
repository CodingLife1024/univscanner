from bs4 import BeautifulSoup
import requests

university = "Harvard"
country = "USA"

def harvard():
    url = "https://www.seas.harvard.edu/computer-science/faculty-research"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        departments = ["Robotics and Control", "Systems, Networks, and Databases"]

        faculty_data = []

        for title in departments:
            department_element = soup.find('a', class_='accordion-title', string=title)

            if department_element:
                # Find the next <div> tag with class 'accordion-content' after the accordion title
                department_content = department_element.find_next_sibling('div', class_='accordion-content')

                if department_content:
                    # Find all <a> tags within the accordion content
                    links = department_content.find_all('a')

                    for link in links:
                        name = link.get_text(strip=True)
                        href = "https://seas.harvard.edu" + link.get('href')

                        try:
                            new_response = requests.get(href)
                            new_response.raise_for_status()

                            new_content = new_response.text
                            new_soup = BeautifulSoup(new_content, 'html.parser')

                            email = new_soup.find('a', class_=None, id=None, href=lambda href: href and href.startswith('mailto:')).get_text()

                            if [university, country, name, email, href] not in faculty_data:
                                faculty_data.append([university, country, name, email, href])
                            print([university, country, name, email, href])

                        except (requests.exceptions.RequestException, AttributeError) as e:
                            print(f"Error processing {name}:", str(e))
                            continue

        print()
        print("Harvard scraping completed.")
        print()
        return faculty_data

    except requests.exceptions.RequestException as e:
        print("Error fetching Harvard faculty page:", str(e))
        return []