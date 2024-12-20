from bs4 import BeautifulSoup
import requests
import pprint
import sys
import os
import re
import concurrent.futures

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.url_generator import get_next_url

url = "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866"

faculty_data = []

def search_individual(person, headers, u_name, country, print_flag=0):
    global faculty_data
    name = person.find('h3', class_='gs_ai_name').text
    link = "https://scholar.google.com" + person.find('a')['href']
    title = person.find('div', class_="gs_ai_aff").text
    low_title = title.lower()

    personal_data = [name, link, title]

    if "professor" in low_title or "lecturer" in low_title and "emeritus" not in low_title:

        new_r = requests.get(link, headers=headers)
        new_soup = BeautifulSoup(new_r.text, 'html.parser')

        homepage = new_soup.find('a', string="Homepage")['href'] if new_soup.find('a', string="Homepage") else "N/A"

        areas_of_expertise = new_soup.find('a', class_='gsc_prf_inta gs_ibl') if new_soup.find('a', class_='gsc_prf_inta gs_ibl') else []

        research_string = "Research:\n" + "\n".join([area.text for area in areas_of_expertise])
        article_string = "Articles:\n"

        all_articles = new_soup.find_all('tr', class_='gsc_a_tr')

        all_articles_info = []

        for article in all_articles:
            title = article.find('a').text
            link = "https://scholar.google.com" + article.find('a')['href']
            research_string = research_string + "\n" + title
            article_string = article_string + "\n" + title
            all_articles_info.append((title, link))

        if print_flag == 1:
            print("===" * 10)
            print("\n")
            print(personal_data)
            print(research_string)
            print(article_string)
            print("\n")
            print("===" * 10)

        all_research = research_string + "\n" + article_string

        found_keyword = any(re.search(re.escape(keyword), all_research, re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:
            author_link = "https://scholar.google.com/citations?hl=en&user=" + link.split("user=")[1].split("&")[0]
            data = [u_name, country, name, "NA", homepage, author_link]
            faculty_data.append(data)
            print(data)

        return personal_data, homepage, research_string, article_string, all_research

def search_faculty_list(url, headers, u_name, country):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_people = soup.find_all('div', class_='gsc_1usr')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_individual, person, headers, u_name, country) for person in all_people]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    return faculty_data, get_next_url(soup)


if __name__ == "__main__":
    search_faculty_list(url, headers, "University of Michigan", "United States")