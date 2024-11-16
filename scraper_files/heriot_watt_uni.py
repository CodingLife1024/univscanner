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

u_name = "Heriot-Watt University"
country = "United Kingdom"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def heriot_watt_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=lW5jAEC4__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=wBEAALDG__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=F3YeAObQ__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=LQwhAPrZ__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=xP1IAPje__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=UGYBAHPi__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=NlPKAFzl__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=cZUGAArp__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=GlqGAFTr__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=88EBAOPs__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=WLMKAH3u__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=TwlNAKPw__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=WMXbAFnx__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=GNVCAPXy__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=Sg1CAJjz__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=J1wAAJr0__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=XUgAAKL1__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=oeo2ACP2__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=LjqEAEP3__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=28MLAKr3__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=YpWHAd33__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=G-uoAH74__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=sjg5AND4__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=k8y2ADL5__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=pidQAJz5__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=ByOwAAD6__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=wayTAJD6__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=2NqQAO36__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=PIQ3ADj7__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=6zQqAHv7__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=W2IsAKL7__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=ytRqAPL7__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=RU8mATn8__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=Ec-mAGP8__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=sz0OAIf8__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=2lyPAJ78__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=n36CANH8__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=Q5sIAPD8__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=vJkxACD9__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=YMEOAUn9__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=Wq_qAG79__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=l07WAJv9__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=M-EPAcL9__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=HN42AeX9__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14625542210134544336&after_author=nuZRAQb-__8J&astart=450',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nHeriot-Watt University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    heriot_watt_uni()