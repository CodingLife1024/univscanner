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

u_name = "National University of Sciences and Technology"
country = "Pakistan"

all_faculty_national_uni_sciences_tech = []

def get_faculty_data(link, headers):
    global all_faculty_national_uni_sciences_tech
    all_faculty_national_uni_sciences_tech += search_faculty_list(link, headers, u_name, country)[0]

def national_uni_sciences_tech():
    global all_faculty_national_uni_sciences_tech
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=JI4DAFPg__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=1HcbABLr__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=CPHiAFHw__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=8nsCAGXz__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=o-kJAFj1__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=6r2oAJT2__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=O18OAU73__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=FDbnAFb4__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=LqQXANL4__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=G23YAF_5__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=8q_KAPL5__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=Tmv1AE76__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=xeMrALL6__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=0lWQACH7__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=ZRYDAHT7__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=sagCAKn7__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=yCOnAPH7__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=EYsZAC_8__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=7r6tAE_8__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=ElfDAHf8__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=S5veALr8__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=ycUNAfT8__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=hxklABX9__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=keiIAS79__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=KJiYAW79__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=3nwNAYn9__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=p8rcALP9__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=gxkQAMz9__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6448869601282236476&after_author=1acCAO39__8J&astart=290',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNational University of Sciences and Technology done...\n")
    all_faculty_national_uni_sciences_tech = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_national_uni_sciences_tech)]
    return all_faculty_national_uni_sciences_tech

if __name__ == "__main__":
    national_uni_sciences_tech()