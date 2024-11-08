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

u_name = "Monash University"
country = "Australia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def monash_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=j1aNAIZU_v8J&astart=10",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=SYEBAPmn_v8J&astart=20",
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nMonash University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    monash_uni()