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

u_name = "University of Newcastle"
country = "Australia"

all_faculty_uni_newcastle = []

def get_faculty_data(link, headers):
    global all_faculty_uni_newcastle
    all_faculty_uni_newcastle += search_faculty_list(link, headers, u_name, country)[0]

def uni_newcastle():
    global all_faculty_uni_newcastle
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=bNpwAJBm__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=rpM8AVSM__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=36MPADui__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=EO4gAE27__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=oykIAP3A__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=UqYQAPPP__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=fcsZAAvW__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=J80GAH3Z__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=B0ofABbc__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=tjY0AJ_g__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=J5FZAPPi__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=0bhSALHl__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=xZQDAI3n__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=muFTAG3p__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=y0oDAIvq__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=6wQMALHr__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=bnAHAYHt__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=qhUSALju__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=KHZtAZnv__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=6vcEAH_w__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=qI0GAJTx__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=6UAxAIDy__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=9AoiAGzz__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=XI64AAP0__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=F_cDAIz0__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=0vGrAOb0__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=RHceAbP1__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=OIFrAA32__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=r4gOAIX2__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=JhRJARn3__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=yAgZAJ73__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=ulJDAPr3__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=6T3YAFP4__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=9RgGANz4__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=PKoVACf5__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=yNatAGL5__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=7ou0AJP5__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=XIkJAND5__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=X-0WAO35__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=WY8fABr6__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=W2AzAGT6__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=b3CpAJP6__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=9TW0AMT6__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=Bk0WAO76__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=O_ZnAB37__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=I5sbAUf7__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=CamEAGn7__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=VghFAJj7__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=4mFnALr7__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=qeZoAOP7__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=2qI_AAn8__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=LEeHASP8__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=3NiaAEj8__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=pc0JAGf8__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=JjaGAKP8__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=cnklALH8__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=PH1-ANT8__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=SXUsAPL8__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=cqodAQP9__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=nR7uACr9__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=JqeIADn9__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=NCeYAFP9__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=nzxvAGX9__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=IpxGAH79__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=9l_CAJv9__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=VKeWAKr9__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=07liAbf9__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=00rLAMj9__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=fcyzAOf9__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=13721485061121641907&after_author=C2rIAPj9__8J&astart=700',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Newcastle done...\n")
    all_faculty_uni_newcastle = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_newcastle)]
    return all_faculty_uni_newcastle

if __name__ == "__main__":
    uni_newcastle()