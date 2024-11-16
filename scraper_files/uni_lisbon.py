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

u_name = "University of Lisbon"
country = "Portugal"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_lisbon():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=gmAoAEmn__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=YWeAAHHE__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=QtQPAGDY__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=m20tAEre__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=d7RFAC7j__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=wfYKAL3m__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=EYsPAJDo__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=1EwrAH_r__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=s3YyAK7t__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=naJZAI3u__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=QNECAN7v__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=oJwyAJrw__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=nqmXAGjx__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=3zsdAEvy__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=EEMJAALz__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=UDiqAMDz__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=4TfhAHv0__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=5r4rABD1__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=jswjAIT1__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=oPFkAPX1__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=NUQIAFr2__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=fv8iALb2__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=rDkZADX3__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=b_YPAOn3__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=Q5WPAHH4__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=ojaqAKz4__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=ZWPzAAH5__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=UfyoAC_5__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=HfMFAHb5__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=Il8DAK35__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=wcs7AAT6__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=OBZSAE36__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=EQUCALT6__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=WDUmAOP6__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=LxlHAET7__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=1XiYAG_7__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=kO4DAKf7__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=fsbIAOr7__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=w1rBABH8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=BB0CADn8__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=LCZ0AEn8__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=vsIBAFz8__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=NWUSAJX8__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=OJ4bAMD8__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=_gatAO78__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=V84TACH9__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=qKPLADb9__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=TP0kAF79__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=w2QqAH79__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=vG6YAJD9__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=ixkUALX9__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=UMtnAMj9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=i3yXANv9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3192267945013080153&after_author=CvKdAOr9__8J&astart=540',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Lisbon done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    uni_lisbon()