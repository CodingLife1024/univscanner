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

u_name = "National Tsing Hua University"
country = "China"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def national_tsing_hua_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=-DVoALWO__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=vug8Afa-__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=Pa55AALQ__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=teP1AATa__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=i-g_AIvd__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=6UuEAP7g__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=B6eTAOfj__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=Z4mTALDn__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=PXQCAC_r__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=fdkIAATt__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=uIWCACfv__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=wi0_AFzw__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=Qn1xAHfx__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=20uCAALz__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=9XCZAMf0__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=e0JKAZb1__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=uZ-eAHr2__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=2vYDACH3__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=10U4ADX4__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=q6NtALL4__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=mHUCACz5__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=qBRJAH_5__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=x_ncAOf5__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=ViUQAUz6__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=prP3ALH6__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=H8RHABj7__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=BdQAAJX7__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=etVgAeP7__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=fX1_ACD8__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=toJMAH38__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=7PYPAMD8__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=_7ZcAAX9__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=czQAACD9__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=7gV6AEj9__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=KTLDAYf9__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=ol7bAMX9__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=iDHeAOv9__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3696850180452525172&after_author=rT8zAAH-__8J&astart=380',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nNational Tsing Hua University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    national_tsing_hua_uni()