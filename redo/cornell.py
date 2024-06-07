import requests
from bs4 import BeautifulSoup
import re

university_name = "Cornell University"
country = "USA"

def cornell():
    # URL of the form submission (same as the homepage in this case)
    urls = [
        "https://www.engineering.cornell.edu/faculty-directory?letter=A",
        "https://www.engineering.cornell.edu/faculty-directory?letter=B",
        "https://www.engineering.cornell.edu/faculty-directory?letter=C",
        "https://www.engineering.cornell.edu/faculty-directory?letter=D",
        "https://www.engineering.cornell.edu/faculty-directory?letter=E",
        "https://www.engineering.cornell.edu/faculty-directory?letter=F",
        "https://www.engineering.cornell.edu/faculty-directory?letter=G",
        "https://www.engineering.cornell.edu/faculty-directory?letter=H",
        "https://www.engineering.cornell.edu/faculty-directory?letter=I",
        "https://www.engineering.cornell.edu/faculty-directory?letter=J",
        "https://www.engineering.cornell.edu/faculty-directory?letter=K",
        "https://www.engineering.cornell.edu/faculty-directory?letter=L",
        "https://www.engineering.cornell.edu/faculty-directory?letter=M",
        "https://www.engineering.cornell.edu/faculty-directory?letter=N",
        "https://www.engineering.cornell.edu/faculty-directory?letter=O",
        "https://www.engineering.cornell.edu/faculty-directory?letter=P",
        "https://www.engineering.cornell.edu/faculty-directory?letter=Q",
        "https://www.engineering.cornell.edu/faculty-directory?letter=R",
        "https://www.engineering.cornell.edu/faculty-directory?letter=S",
        "https://www.engineering.cornell.edu/faculty-directory?letter=T",
        "https://www.engineering.cornell.edu/faculty-directory?letter=U",
        "https://www.engineering.cornell.edu/faculty-directory?letter=V",
        "https://www.engineering.cornell.edu/faculty-directory?letter=W",
        "https://www.engineering.cornell.edu/faculty-directory?letter=X",
        "https://www.engineering.cornell.edu/faculty-directory?letter=Y",
        "https://www.engineering.cornell.edu/faculty-directory?letter=Z"
    ]

    full_text = ""

    for link in urls:
        response = requests.get(link)
        full_text += response.text

    soup = BeautifulSoup(full_text, 'html.parser')

    faculty_data = []
    faculty_divs = soup.find_all('div', class_='faculty-bio-all')

    for faculty_div in faculty_divs:
        name_tag = faculty_div.find('h2', class_='person__name').find('a')
        name = name_tag.text.strip()
        profile_url = name_tag['href']

        new_r = requests.get(profile_url)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        depts = new_soup.find_all('li', class_=None)

        departments = ['Computer Engineering', 'Computer Systems', 'Integrated Circuits', 'Systems and Networking']

        for dept in depts:
            dd = dept.text.strip()
            if dd in departments:
                email = faculty_div.find('div', class_='person__email').text.strip() if faculty_div.find('div', class_='person__email') else "Email Not Found"

                # pers_link = faculty_div.find(lambda tag: tag.name == 'h2' and 'class' not in tag.attrs and tag.string == 'Websites').find_next('a')['href']


                if [university_name, country, name, email, profile_url] != faculty_data[-1] if faculty_data != [] else True:
                    faculty_data.append([university_name, country, name, email, profile_url])
                    print([university_name, country, name, email, profile_url])
                    print()

    print()
    print('Cornell done...')
    print()
    return faculty_data

# cornell()