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

u_name = "Universität Jena"
country = "Germany"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_jena():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=cwBCAPBd__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=IQxXAK-f__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=UcVUALyw__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=jXWMAMLC__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=vkI4ATjL__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=rz1LAITR__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=scAFANDY__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=r7oHAKzd__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=8aVBAHTj__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=NfwEAJzn__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=waq3ASHq__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=JugHAJ_t__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=z899ADHv__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=pWk-ASjx__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=ueVvALPy__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=XjUCAF30__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=rdgyAFX1__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=UssTAD_2__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=WmGgAPH3__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=evhJAX_4__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=GUYXAEf5__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=oksWAML5__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=neEiAS_6__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=WjsIAJP6__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=MRoXAAL7__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=SGSYAG37__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=bECMAMP7__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=GVnwAP_7__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=qFS7ADf8__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=6gZrAHn8__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=UBlpAb78__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=1YoOAB_9__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=WK9uAU79__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=_78FAGn9__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=izrHAJv9__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=kefxAN_9__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=7635421682074704868&after_author=SB7WAP39__8J&astart=370',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversität Jena done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_jena()