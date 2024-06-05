from bs4 import BeautifulSoup
import requests

university = "Nanyang Technological University"
country = "Singapore"

def ntus():
    url = "https://www.ntu.edu.sg/computing/our-people/faculty"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    # Find all <h3> elements with class 'img-card__title'
    professor_elements = soup.find_all('div', class_='img-card__body')

    for professor_element in professor_elements:
        # Find the <a> tag within each <h3> element
        a_tag = professor_element.find('a')
        if a_tag:
            # Extract the text and the 'href' attribute value
            professor_name = a_tag.get_text(strip=True)
            professor_link = a_tag['href']
            dept = professor_element.find('span', class_='interests').get_text(strip=True) if professor_element.find('span', class_='interests') else "Email Not Found"
            # print("Name:", professor_name)
            # print("Link:", professor_link)
            # print("Departments:", dept)

            found_keyword = any(keyword.lower() in dept.lower() for keyword in keyword_list)

            if found_keyword:
                new_r = requests.get(professor_link)
                new_soup = BeautifulSoup(new_r.text, 'html.parser')

                a_tag = new_soup.find('a', href=lambda href: href and href.startswith("mailto:"))

                if a_tag:
                    email = a_tag.get_text(strip=True)
                else:
                    email = "Email Not Found"

                web_tag = new_soup.find('span', string='Website')

                if web_tag:
                    # Get the parent <a> tag
                    aa_tag = web_tag.find_parent('a')

                    if aa_tag:
                        personal_webpage = aa_tag['href']
                    else:
                        personal_webpage = "Personal Webpage Not Found"


                # print("Email:", email)
                # print("Personal Webpage:", personal_webpage)

                print([university, country, professor_name, email, professor_link, personal_webpage])
                faculty_data.append([university, country, professor_name, email, professor_link, personal_webpage])

    print()
    print("NTUS done...")
    print()

# ntus()
