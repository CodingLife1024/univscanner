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

u_name = "University of Centrale"
country = "France"

all_faculty_uni_centrale = []

def get_faculty_data(link, headers):
    global all_faculty_uni_centrale
    all_faculty_uni_centrale += search_faculty_list(link, headers, u_name, country)[0]

def uni_centrale():
    global all_faculty_uni_centrale
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=m46OAOfT__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=aXoRAGLr__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=wCd8AUXv__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=qujdAN3y__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=WX0MAEL2__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=J8w8AG_4__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=886jAG_5__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=M-G0AG_6__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=qUCDADr7__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=4jheAPj7__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=78MeAMP8__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=g4K2AEj9__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=oZE_AJb9__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8396635836008252311&after_author=BUAjAO79__8J&astart=140',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Centrale done...\n")
    all_faculty_uni_centrale = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_centrale)]
    return all_faculty_uni_centrale

if __name__ == "__main__":
    uni_centrale()