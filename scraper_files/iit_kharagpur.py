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

u_name = "Indian Institute of Technology, Kharagpur"
country = "India"

all_faculty_iit_kharagpur = []

def get_faculty_data(link, headers):
    global all_faculty_iit_kharagpur
    all_faculty_iit_kharagpur += search_faculty_list(link, headers, u_name, country)[0]

def iit_kharagpur():
    global all_faculty_iit_kharagpur
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=LIdrAHzE__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=biwAAKTQ__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=EaYrAGfX__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=jk8HAKPc__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=D7MxAE_h__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=2Vs5AKLk__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=N9klAHPn__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=zfkGAB_q__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=y4QJAOTr__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=bnQTAIPt__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=Nxg1ALLu__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=uuMAAKPv__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=pPMTAHrw__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=a_sZAUzx__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=1Aw6AB_y__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=6mGKAAPz__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=t3gDACD0__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=3J2UAA71__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=oBZqAPj1__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=uRcEAFD2__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=sjohAOT2__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=QrAFAF_3__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=mRmaALv3__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=dtAJACr4__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=t7YRAKv4__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=hySRANv4__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=bqeAAAH5__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=PcW-AUz5__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=JXCqAcb5__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=4LsLABj6__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=zqoIAFz6__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=i6J2AJ76__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=tK5CAOP6__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=PYssACX7__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=xHdSAGX7__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=WLLBAI37__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=6p4OALf7__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=GSRRANj7__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=bA66ACj8__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=3mSQAFn8__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=W7HeAHr8__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=9yI3AJz8__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=GMP8AOD8__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=QoETAO78__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=FFWZAAz9__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=UKNcADD9__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=H-2nAEn9__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=ZWQZAGH9__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=uOgFAG79__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=klUWAJv9__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=JdDaALz9__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=gIYIAdX9__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=awkLAe39__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9904414229552554802&after_author=U9JsAAn-__8J&astart=540',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nIndian Institute of Technology, Kharagpur done...\n")
    all_faculty_iit_kharagpur = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_iit_kharagpur)]
    return all_faculty_iit_kharagpur

if __name__ == "__main__":
    iit_kharagpur()