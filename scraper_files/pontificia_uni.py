import concurrent.futures
import os
import pprint
import re
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.gscholar_indiv_page import search_faculty_list

u_name = "Pontificia Universidad Catolica de Chile"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def pontificia_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=pontificia+university&btnG=",
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=cDSHAAnp__8J&astart=10',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=dGECAP7t__8J&astart=20',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=_pIcAMLy__8J&astart=30',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=YoUQALX1__8J&astart=40',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=dnQNAdj3__8J&astart=50',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=Z7eiAPr4__8J&astart=60',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=gfOQAPn5__8J&astart=70',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=5tULAEn7__8J&astart=80',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=UzJxAL_7__8J&astart=90',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=cok8AET8__8J&astart=100',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=bp8XAJH8__8J&astart=110',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=pjUgAfH8__8J&astart=120',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=V2UAAWv9__8J&astart=130',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=l0CGAKf9__8J&astart=140',
        'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=pontificia+university&after_author=pCEOAfL9__8J&astart=150',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nPontificia Universidad Catolica de Chile done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    pontificia_uni()