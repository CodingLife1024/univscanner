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

u_name = "Kyushu University"
country = "Japan"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def kyushu_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=IR24AGuV__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=NomSACi___8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=3-n5AJbJ__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=KQGTADXQ__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=VvdEANfV__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=NXsDAHPa__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=KLVYAdnf__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=UtSDALjh__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=UGePADTk__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=Ji06ACDm__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=u4JcAAfo__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=CKdXASXq__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=xPCaAAHs__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=Qg-IAJ3t__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=ucTvAKbu__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=wWGGAPDv__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=ztDPAK3w__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=dIvRAKLx__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=IcINAYDy__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=BXkKAE_z__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=8byDABb0__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=XU2AAMX0__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=InQ8ADT1__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=_wdvAd71__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=bsGVAEL2__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=CD-XALv2__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=oRRjACz3__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=c2UtAIn3__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=LbqYALn3__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=SMN9ADL4__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=LDGBAK74__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=7IzOAAL5__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=qDsAAD35__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=O2CBAJL5__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=AwhbAML5__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=c2i0APj5__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=Gly5AVD6__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=6LJNAHr6__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=jssfAKv6__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=UrPjAOD6__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=LHJ7AST7__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=C84CAGv7__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=l85QAa_7__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=LUXOAdT7__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=eHHCAQf8__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=kZP-ADD8__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=YdtRAV38__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=MtdcAZH8__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=lcUqAcP8__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=X-_YAPb8__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=rXszASP9__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=UpizAE39__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=SY8-AHH9__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=D_lqAIn9__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=ekmSALT9__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=TAfAAdL9__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6919135986770139700&after_author=D-aOAfP9__8J&astart=570',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nKyushu University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    kyushu_uni()