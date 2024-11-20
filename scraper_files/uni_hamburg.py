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

u_name = "University of Hamburg"
country = "Germany"

all_faculty_uni_hamburg = []

def get_faculty_data(link, headers):
    global all_faculty_uni_hamburg
    all_faculty_uni_hamburg += search_faculty_list(link, headers, u_name, country)[0]

def uni_hamburg():
    global all_faculty_uni_hamburg
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=D2sCABCq__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=RCGQAd-9__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=X4JxAKTL__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=gh4IAAfT__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=HWsxACfd__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=ov0JAPTg__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=bhsVAFrl__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=OJPJAAjn__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=vp1HAb3p__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=7LMJANrs__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=iLfPAUTu__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=F0MdAEXw__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=YR3bAJ7x__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=QZOBAXLz__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=KLrDAGL0__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=Wa2IAPj1__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=92KAAKr2__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=UhYvAP72__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=KC-ZALn3__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=Lm_TAGH4__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=g3IEANX4__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=exUYAKv5__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=KNfKAB76__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=Aj0OAWr6__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=SxJ0AKr6__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=xaoPAAj7__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=7tjuAGP7__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=saHNAMb7__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=HsKFAP_7__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=79YeAEj8__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=OlggAIT8__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=G6kAALL8__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=bqPVAOP8__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=NO4HABj9__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=nIeaADj9__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=0HcVAWb9__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=CsvYAIr9__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=p6z_AMP9__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=t4VDAer9__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=ta6EAff9__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10848167875220160520&after_author=IHMuAAn-__8J&astart=410',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Hamburg done...\n")
    all_faculty_uni_hamburg = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_hamburg)]
    return all_faculty_uni_hamburg

if __name__ == "__main__":
    uni_hamburg()