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

u_name = "University of North South Wales"
country = "Australia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_north_south_wales():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=cnYWABAn_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=a7mKAD8l__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=IQMCABJX__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=gWoaALpq__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=P1AOAKh9__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=dS1_AICK__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=JNwPAAGS__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=qy0BAF-e__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=uaz4ANOn__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=5voEAD-v__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=ZFQdAI-y__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=odghANW3__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=6_xtAXm8__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=8scLAIy-__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=NNEdACzB__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=3UYIAMPD__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=t6HHAVzH__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=TFo-AAvJ__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=d2dFALvK__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=5dh5AFXM__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=xf2MAAHO__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=R5YcAH_P__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=NaEAAE7R__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=nF5bAAbT__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=t18cAKbU__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=-bQQAIHV__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=mtYCAP3W__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=b7lZAHbY__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=8QYcAEHa__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=jHhGAGvb__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=zz42ACfd__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=kgd4AIXe__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=2rljAF3f__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=IHqCAOzf__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=LUhBAOTg__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=ShgXAGzh__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=aXkEADXi__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=mi2zAKfi__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=iMf5ALPj__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=ZT9NAC7k__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=zUTbACvl__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=HEJpALHl__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=Kqt4AHHm__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=UauIAGvn__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=JogMAP_n__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=s8pmAG3o__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=kqEBACbp__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=hlYkAKLp__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=mLBGATXq__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=ocERAG3q__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=WEVmALTq__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=m7wXAB7r__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=ZygjAJbr__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=n34kAMTr__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4274056836244091944&after_author=HvV9AD_s__8J&astart=550',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of North South Wales done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_north_south_wales()