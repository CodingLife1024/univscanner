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

u_name = "University of Bergen"
country = "Norway"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_bergen():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=8898899287978071111",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=wZHmABdK__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=3jafAXqS__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=dHgpAGep__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=cKoCAPe5__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=OqxgADXD__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=zTIBAEbI__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=zeFcAI7O__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=KkAyAEDU__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=ufMsAMjY__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=ZQdZALDe__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=JBVFAPzg__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=yb8dAM_k__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=OFggAFLo__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=mXwRAIHp__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=XbSuAJLq__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=rLAcAGfr__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=RTQFAFvs__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=HJIBADLu__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=0YxbAAfv__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=nqoCAPDv__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=76sAAK3w__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=G_5rAAfx__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=KBFWAMjx__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=KbBOACHz__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=70kIAPrz__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=QYYIATr0__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=k3pwAP30__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=Z-4JAEj1__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=9iRrAMb1__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=KY4DADX2__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=XNRlAb32__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=HMM4ADP3__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=rW2CAIr3__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=-9EAAPb3__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=lm42AD_4__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=bjUSAIv4__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=C5HBALn4__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=9JWKACD5__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=tTNfAXD5__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=frVCAJ_5__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=FM99AOf5__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=DnPOACT6__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=myVtAWD6__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=VfchAaT6__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=nAxCAcD6__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=orCxARb7__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=EV9BAEL7__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=pKpSAXT7__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=yFcJAL77__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=ngMRAPn7__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=XpVaABX8__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=uQeJAUz8__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=pWy3AHH8__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=LLWpAaD8__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=yv9DAMD8__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=PmR8AOb8__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=yRn2ABH9__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=7vSAAD39__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=DoWyAFT9__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=sj0aAG79__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=0W-mAJD9__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=OUR_AKv9__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=UrteAMb9__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=Gg8dAOD9__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=QToAAfH9__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8898899287978071111&after_author=JcI-AQH-__8J&astart=660',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Bergen done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    uni_bergen()