import requests
from bs4 import BeautifulSoup

u_name = "University of Queensland"
country = "Australia"

def uni_queensland():
    url = "https://eecs.uq.edu.au/about/our-people"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    headings = soup.find_all('h3', class_=None)

    titles = ["Dr ", "Miss ", "Professor ", "Associate Professor ", "Mrs ", "Mr "]

    for heading in headings:
        # print(heading.text.strip())
        heading_text = heading.text.strip()
        if heading_text not in ["Research staff", "Professional staff", "Honorary, adjunct, emeritus staff", "Cyber security and software engineering team", "Data science team", "Engineering and Technical Support Group", "UQ Cyber Security"]:
            print(f"\n{heading_text}\n" + "-"*len(heading_text) + "\n")

            professor_list = heading.find_next('ul', class_="vertical-list vertical-list--ruled")

            if professor_list:
                professors = professor_list.find_all('div', class_="person--teaser")

                for professor in professors:
                    name = professor.find('a').text.strip()
                    for title in titles:
                        if name.startswith(title):
                            name = name[len(title):]
                    link = "https://eecs.uq.edu.au" + professor.find('a')['href']
                    print(f"{name}: {link}")
            else:
                print("No professors found under this heading.")

uni_queensland()
