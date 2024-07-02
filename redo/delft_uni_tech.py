import requests
import re
from bs4 import BeautifulSoup
import google_scholar

u_name = "Delft University of Technology"
country = "Netherlands"

def decode_email(encoded_email):
    """Decode the email address from the HTML character codes"""
    decoded_email = ''.join([chr(int(code)) for code in re.findall(r'&#(\d+);', encoded_email)])
    return decoded_email

def delft_uni_tech():
    url = "https://www.tudelft.nl/en/eemcs/the-faculty/professors"   # homepage url
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction"]

    faculty_data = []

    professor_blocks = soup.find_all("div", class_="profile theme-blue hoverableBlock hoverableBlock--green hoverableBlock--hasLink")

    for block in professor_blocks:
        name_element = block.find("h3")
        if name_element:
            name = re.sub(r'Prof\.dr\.ir\.|Prof\.dr\.', '', name_element.text).strip()
            profile_link = block.find("a", href=True)["href"] if block.find("a", href=True) else None

            if profile_link:
                new_r = requests.get(profile_link)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                email = new_soup.find('a', class_='i-mail')['href'][7:] if new_soup.find('a', class_='i-mail') else None

                expertise = ""

                expertise_element = new_soup.find_all("a", class_="btn btn--orange btn--borderBox color-white btn--single")
                for element in expertise_element:
                    expertise += element.text.strip().lower()


                print(name, profile_link, email, '\n\n', expertise, '\n\n')



delft_uni_tech()

