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

u_name = "RWTH Aachen University"
country = "Germany"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def rwth_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=bLGHALUa__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=SEclABF3__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=bjgPAAmX__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=b_oNANeq__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=luKWANu1__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=wfVDAcDA__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=0FisAHzF__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=1qINAODO__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=kJAfAPDT__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=Aqr5AO_W__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=QOs8AGba__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=1Td1AKrd__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=DaO8AK7g__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=yA1xABTj__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=QFwpAWzk__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=HQNpAGbm__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=KD4AANvn__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=lbqnADXq__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=NGcJADbr__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=XAQjANLs__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=xP0AAKTt__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=sIsCAPDu__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=pSr3AN7v__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=UvV-AMTw__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=5MweAH7x__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=kOuNAGDy__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=lURJAPny__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=HIsoALzz__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=CtGNAdL0__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=YnL1AID1__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=4dlQAAH2__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=QHQBAGz2__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=_lBnAN32__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=w5V_AI33__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=-6wGABP4__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=f3p5AJ_4__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=94MeAdb4__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=XR6RABv5__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=5zgQAWn5__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=VjpMAK35__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=H-Q3Ae35__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=Z3wVAE_6__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=mUiUAJj6__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=ov4QALf6__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=1AlCAPr6__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=h4QDACb7__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=6xfdADv7__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=1KyTAHf7__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=8M-eAJH7__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=obeDAMb7__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=ewvCAA78__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=G-llADb8__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=KzLEAG38__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=-fMAAJf8__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=7Mu4AKL8__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=s3-ZAcP8__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=THcxAOb8__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=OIknAPz8__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=HfCuAAn9__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=VOQGACb9__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=yaPqAEH9__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=PmcJAGD9__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=0C9YAXX9__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=bAHcAIT9__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=pBr1AJb9__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=iQOtAKT9__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=xb1GAb39__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=7yrDAM39__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=pYWEAeP9__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=U5gQAPD9__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=2022388551903139277&after_author=lAAqAfz9__8J&astart=710',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nRWTH Aachen University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    rwth_uni()