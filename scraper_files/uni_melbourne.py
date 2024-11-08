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

u_name = "University of Melbourne"
country = "Australia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_melbourne():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ACAeADKn_v8J&astart=10",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=nrWCAGj9_v8J&astart=20",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=N6YAAPhB__8J&astart=30",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=k8AEAJRh__8J&astart=40",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=9W8xAJBy__8J&astart=50",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=yrJ8AH-I__8J&astart=60",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=nfMKAAeP__8J&astart=70",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=4asHAD6W__8J&astart=80",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=Vc4MAMWc__8J&astart=90",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=kStbAF-e__8J&astart=100",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=bKggAMOi__8J&astart=110",
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Melbourne done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_melbourne()