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

u_name = "University of Melbourne"
country = "Australia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_melbourne():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ACAeAAKn_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=nrWCAGj9_v8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=N6YAAPhB__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=k8AEAHhh__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=9W8xAIty__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=yrJ8AG2I__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=nfMKAAeP__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=4asHADmW__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=Vc4MAMWc__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=kStbAFme__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=bKggALei__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=l3M7AHuo__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=iydQAdKr__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=Uc4CAHGt__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ybMBAAqy__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=VWy0ACK1__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=l5YVAHS3__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=pMZzAJe5__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=Js0BADu8__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=tcd6AI--__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=Ao25AC7B__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=GA__AALD__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=RmcPAA_G__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=V5TUANvH__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ba4fAMPI__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=86oaAFLK__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=q7Q1AEDM__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=isxpAa3N__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=J28DAEbP__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=WP4YALXQ__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=gNqtACLR__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=mBz1ADjS__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=RZV-AHTT__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=6TcHAVHU__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=4jcOADPV__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=sMxCAM3V__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=pnFSALTW__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=JDABAHjX__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=JOtDAAXY__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=nHotAOTY__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=a96GAHva__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=q7i_AAzb__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=gGVnAB3c__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=45ajAADd__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=FI2yAO3d__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ZHQKANHe__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=urIbAKPf__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=BDlUAA7g__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ngIvAHXg__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=rl0lACLh__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=NcwDAJLh__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=nh8SAHLi__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=QfccAO3i__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=tF1oAGjj__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=e-wAANLj__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=2G4DADvk__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ni8iAJvk__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=-F-NAHLl__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=axTgAMfl__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=4KopAB7m__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=CUAHAG7m__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=4dcNAPDm__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=cy3tAFfn__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=raB9AMHn__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=G04WABzo__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=GNwAAHzo__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=R48VAf_o__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=cv4CAHTp__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=xWMMAOnp__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=-qCJACPq__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=ZpioAdHq__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=j51FAELr__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=xIMqAY_r__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10194437184893062620&after_author=zV0BABTs__8J&astart=740',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Melbourne done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_melbourne()