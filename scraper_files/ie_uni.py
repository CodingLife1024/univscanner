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

u_name = "IE University"
country = "Spain"

all_faculty_ie_uni = []

def get_faculty_data(link, headers):
    global all_faculty_ie_uni
    all_faculty_ie_uni += search_faculty_list(link, headers, u_name, country)[0]

def ie_uni():
    global all_faculty_ie_uni
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=lNSFAHLv__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=AbliAJT2__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=c_hLALH5__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=J78_AD_7__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=BiU9AJ78__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=Nd88ASj9__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=aiF5AOP9__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=JYetACD-__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=ffdUAKP-__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=9wSCAN_-__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=kXP7ACr___8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=9oj-AEn___8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=JJScAGT___8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=aEpzAaH___8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=JzSAAL3___8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=aoY9Acf___8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=dnqZAOT___8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=E-KFAfD___8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=17142240565581583084&after_author=SCmHAfr___8J&astart=190',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nIE University done...\n")
    all_faculty_ie_uni = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_ie_uni)]
    return all_faculty_ie_uni

if __name__ == "__main__":
    ie_uni()