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

u_name = "University of Waikato"
country = "New Zealand"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_waikato():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=J8SEADG1__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=vWgGAO_N__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=ntsPAGni__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=jAmAAHLn__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=pWEhALfr__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=-ToEAFnu__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=gzk7ADzx__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=WzgGAFTy__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=jU8DAaH0__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=oVMeAI71__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=2SMDAIv2__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=nyGVAH33__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=CnEQAHj4__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=LxaXAeL4__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=5HMTADX5__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=JibvABL6__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=kJsAAJb6__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=jJQAADz7__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=EFkBAIf7__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=D-CYAPv7__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=WFo7AED8__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=pwD-AJf8__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=RtVnAAD9__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=MpwBAFP9__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=mcoaALT9__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=jJ82ANH9__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4465814664967962113&after_author=m80mAQn-__8J&astart=270',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Waikato done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    uni_waikato()