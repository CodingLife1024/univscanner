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

u_name = "Qatar University"
country = "Qatar"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def qatar_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=XclhAFK1__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=43EbALPA__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=7w4rANrS__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=rD8CAMrZ__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=wiA9ALnf__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=gbN8AJri__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=CLcjAGrm__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=J42bAFHo__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=7LAyAFzq__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=LUg8AFPs__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=Tb5aAGnt__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=0_xLANPu__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=bpEOAOzv__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=xxIRAPnw__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=eNVRARny__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=TySjACDz__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=utMgAOnz__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=sp7JALb0__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=JWgzAF31__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=qeQBAD_2__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=IgtIAP_2__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=QrUuALX3__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=y4kOASD4__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=fc1xAGL4__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=UX4uANX4__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=tMr-AD_5__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=bAlZAI_5__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=CrKsANn5__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=VFAOATH6__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=YkYKAZf6__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=1SPCAOP6__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=wYNHAC37__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=kvhRAFT7__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=h0p8AIX7__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=SG6GAMn7__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=UYrKAB38__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=YPBKAEv8__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=f3s3AYT8__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=zxRsAKb8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=tGlvAcP8__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=IAA0ANj8__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=EUcQABr9__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=WVw3AUH9__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=PzyeAGL9__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=95Y9AIz9__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=2JGdAKX9__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=ftZxAL_9__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=sYMyAdD9__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=TF_ZAOj9__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=MmEhAf39__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18228365631054052488&after_author=SGwzAAf-__8J&astart=510',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nQatar University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    qatar_uni()