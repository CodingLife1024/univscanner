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

u_name = "Tomsk State University"
country = "Russia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def tomsk_state_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=wS97ALPt__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=Xh97AOrx__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=Jnd9AND0__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=bfp6AFr2__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=RTJ7AFT3__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=DCd7ANr3__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=SKB7AI_4__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=q1p8AIb5__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=KSl7AL35__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=9nZ9ACH6__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=OFt8AMH6__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=ERR7AD77__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=nHF8AID7__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=_l98AKP7__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=CV98AO77__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=_H17ADn8__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=oV98AF_8__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=Efd7AJr8__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=-H17AMf8__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=NHl9ANn8__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=O-x6APD8__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=s_t6ABf9__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=bn19ACz9__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=RXt9AEz9__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=0Ht9AGj9__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=U-57AH_9__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=q198AJP9__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=L-g_Aa39__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=u9olAL_9__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=Tnt9AM79__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=93d9AN_9__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1358949768769161856&after_author=fV98APD9__8J&astart=320',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nTomsk State University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    tomsk_state_uni()