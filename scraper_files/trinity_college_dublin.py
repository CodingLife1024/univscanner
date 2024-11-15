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

u_name = "Trinity College Dublin"
country = "Ireland"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def trinity_college_dublin():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=pe4eAHtK__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=_XoDAO9-__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=f42nAPyf__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=pecQAFO0__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=Bz4AAKC7__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=JxumAJTB__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=RT1RAITI__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=tw9bAdDP__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=2fEbACPU__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=ibAAANLY__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=-cRGAPnb__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=XycFAL3d__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=mf5IAK3f__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=R1sCAN7h__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=Ubb-ALjj__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=CXlmAY7l__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=YrY0AL7m__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=4W9JAZTn__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=EygFAJ_o__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=t-A_AArq__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=YrsPAcrq__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3625276516933484551&after_author=miUWABLs__8J&astart=220',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTrinity College Dublin done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    trinity_college_dublin()