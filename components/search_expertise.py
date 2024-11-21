from bs4 import BeautifulSoup
import requests
import pprint
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.url_generator import get_next_url

url = "https://scholar.google.com/citations?hl=en&user=3VpkJSAAAAAJ"

def search_expertise(url, headers):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    
    areas_of_expertise = soup.find('a', class_='gsc_prf_inta gs_ibl') if soup.find('a', class_='gsc_prf_inta gs_ibl') else []

    research_string = "Research:\n" + "\n".join([area.text for area in areas_of_expertise])
    article_string = "Articles:\n"

    all_articles = soup.find_all('tr', class_='gsc_a_tr')

    all_articles_info = []

    for article in all_articles:
        title = article.find('a').text
        link = "https://scholar.google.com" + article.find('a')['href']
        research_string = research_string + "\n" + title
        article_string = article_string + "\n" + title
        all_articles_info.append((title, link))

    all_research = research_string + "\n" + article_string

    return all_research

if __name__ == "__main__":
    print(search_expertise(url, headers))
