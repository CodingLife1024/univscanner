import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

faculty_data = []

u_name = "King's College London"
country = "United Kingdom"

def get_faculty_data(prof):
    a_tag = prof.find("a", class_="block--people-listing__photo")
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

    total_text = ""

    for url in urls:
        r = requests.get(url)
        total_text += r.text

    soup = BeautifulSoup(total_text, "html.parser")

    # Find all list items with role="listitem"
    all_profs = soup.find_all("li", role="listitem")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, prof) for prof in all_profs]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print()
    print("King's College London done....")
    print()
    return faculty_data

if __name__ == "__main__":
    kings_college()