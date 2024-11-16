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

u_name = "Harbin Institute of Technology"
country = "China"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def harbin_institute_tech():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=t5EiAFGA__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=JlGxAPiW__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=VRAIAHK0__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=hBwFAMHD__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=oBxVAAHO__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=SUJAAJfU__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=CswPAK_a__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=bFEHAD7e__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=8zopAGXh__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=AQ6QAf3j__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=g2y1ANfl__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=91zCAAHn__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=D93KANHo__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=rU5RAG3p__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=fjwMAA_r__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=VN8wAKLs__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=JaG2ALbt__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=IZZiACfv__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=VYcLADjw__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=oWAgABDx__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=yTQnAc3x__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=SP2qAIDy__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=8QRVAETz__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=DqRLAM3z__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=WTKvADv0__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=gBNXAaD0__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=d5M3ANb0__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=bKk0ATz1__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=xn8KALT1__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=pzySABD2__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=8wYBAWL2__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=-4YSALv2__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=hqqQAD_3__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=mIaAAJP3__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=rhH8AO33__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=mh4SAEP4__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=otnwAKv4__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=PMxpAPL4__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=8w_FAA_5__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=sei1AFr5__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=C7X3AHv5__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=drTZAKj5__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=cfGgAd_5__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=g3dEABX6__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=Aj8AATX6__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=TAS1AXD6__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=XaDDAKX6__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=LMPnAMf6__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=fFW3APv6__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=y6pGASn7__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=SEzhAGT7__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=e8WFAH77__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=tazBAZ37__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=cYrYAKr7__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=qhVOANb7__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=id24APj7__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=fUOKAST8__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=FGMQAD38__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=vIi6AFr8__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=HT1oAHH8__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=lnZOAI38__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=RlwlAKD8__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=babQAK_8__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=SZYKAMP8__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=hC6PANP8__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=9aBAAf78__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=xmi3ACP9__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=vab7AD_9__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=JGZ-AUz9__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=KA_9AHb9__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=_ycFAYz9__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=PqNpAJ_9__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=BV7JAK79__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=qwJXAbj9__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=vj1pAMj9__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=9HtxAdz9__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=3D2aAPX9__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4726995703083099959&after_author=wj9vAQP-__8J&astart=780',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nHarbin Institute of Technology done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    harbin_institute_tech()