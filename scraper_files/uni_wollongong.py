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

u_name = "University of Wollongong"
country = "Australia"

all_faculty_uni_wollongong = []

def get_faculty_data(link, headers):
    global all_faculty_uni_wollongong
    all_faculty_uni_wollongong += search_faculty_list(link, headers, u_name, country)[0]

def uni_wollongong():
    global all_faculty_uni_wollongong
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=14993595609467436432",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=SwMuASeB__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=dA8MAH6a__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=cb9QAMSw__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=s6ZwADfA__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=N-GlAerG__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=ame4ABzM__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=1-0uAGzQ__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=RDk0AI_T__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=dfV7AOXY__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=s66OAMTd__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=Ui9MADDh__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=sLpQAM3j__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=11itABvl__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=astEABDm__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=IapMAD7o__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=gN8rAOPp__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=hkXoAJTr__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=xSjuAIvs__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=sHYIAHDt__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=y2PBAEjv__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=ImNUAIXw__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=hkgSADDx__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=pxd8AHHy__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=c3BiANHy__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=7ojgAIDz__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=GwUfADf0__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=fREzANT0__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=GbQXAB_1__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=JcAUAKX1__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=8yBoABL2__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=S1wKALT2__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=eMIRAEL3__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=np6nAIX3__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=7pJ-Abv3__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=319IAfj3__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=VhoMAFP4__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=U4sWALj4__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=yWSaABX5__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=ckimAF35__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=fRESAI35__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=S8MEAOf5__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=wKGBAVL6__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=FVMVAJv6__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=RAwgAcH6__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=_S6NAPb6__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=wRl0ACf7__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=kdm4AG37__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=F6FyAIr7__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=VNm4AKf7__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=qO_bANH7__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=0pFzABT8__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=LHsFADT8__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=kTGFAFf8__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=NWcKAGf8__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=M4_AAJT8__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=YP9pAK_8__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=pOCnANr8__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=csxMAPL8__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=XqyhAAr9__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=4mbOACX9__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=wHwGADr9__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=i0hBAVv9__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=IIEKAXH9__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=4lGpAIv9__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=vSoHAJz9__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=sPcnALX9__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=NVgVAMT9__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=4_xAANj9__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=17CWAOb9__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=14993595609467436432&after_author=OEfTAPX9__8J&astart=700',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Wollongong done...\n")
    all_faculty_uni_wollongong = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_wollongong)]
    return all_faculty_uni_wollongong

if __name__ == "__main__":
    uni_wollongong()