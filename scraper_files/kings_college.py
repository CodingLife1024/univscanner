import requests
from bs4 import BeautifulSoup
import re
from redo.google_scholar import get_scholar_profile  # Assuming google_scholar is a valid module

u_name = "King's College London"
country = "UK"

def kings_college():
    urls = [
        'https://www.kcl.ac.uk/informatics/about/people?role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=2&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=3&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=4&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=5&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=6&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=7&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=8&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=9&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics',
        'https://www.kcl.ac.uk/informatics/about/people?page=10&role=Teaching-fellows,Researchers,Visiting,Affiliates,Academics'
    ]

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    faculty_data = []

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        # Find all list items with role="listitem"
        list_items = soup.find_all("li", role="listitem")

        for item in list_items:
            # Find the anchor tag with the class "block--people-listing__photo"
            a_tag = item.find("a", class_="block--people-listing__photo")
            if a_tag:
                name = a_tag["title"]
                if name.startswith("Dr"):
                    name = name[3:]

                link = "https://www.kcl.ac.uk" + a_tag["href"]
                # print(name, link)

                new_r = requests.get(link)
                new_soup = BeautifulSoup(new_r.text, "html.parser")

                biography = new_soup.find("p", class_="Paragraphstyled__ParagraphStyled-sc-176xsi4-0 cgUnvG")
                if biography:
                    biography = biography.text

                research_interests = new_soup.find("ul", class_="UnorderedListstyled__UnorderedListStyled-sc-96evio-0 kUswtk")
                if research_interests:
                    for interest in research_interests.find_all('li'):
                        biography += interest.text

                found_keyword = any(re.search(re.escape(keyword), biography) for keyword in keyword_list)

                if found_keyword or True:  # Adjust this condition as needed

                    email = new_soup.find('div', class_='contact-link icon-email')
                    email = email.text if email else None

                    websites = new_soup.find('a', string=lambda text: text and ('Personal website' in text or 'Research Profile' in text))

                    if websites:
                        personal_link = websites['href']
                    else:
                        personal_link = get_scholar_profile(name)

                    print([u_name, country, name, email, link, personal_link])
                    faculty_data.append([u_name, country, name, email, link, personal_link])

    print()
    print("King's College London done....")
    print()
    return faculty_data
