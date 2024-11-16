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

u_name = "Vrije University of Amsterdam"
country = "Netherlands"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def vrije_uni_amsterdam():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=UpAIAOS9_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=u_oDAHxW__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=gn0ZANdz__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=A4kBAO6K__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=0vgCAKeg__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=iyUAAKe0__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=gEEYAGW8__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=TFsDAMHD__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=F4AhABLH__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=-6qyAJTJ__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=m0eqAEbM__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=rYUCANPQ__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=pSQJAFTU__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=-EzdADjX__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=OXpEACPa__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=hL0FAFDc__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=K58CAHTe__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=z8UHANTg__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=1ScFAGXi__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=7xk6ATbk__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=idlDAJbl__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=6kgCALTm__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=XssDAFvo__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=vtcaAKXp__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=h9ATAFfq__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=tcEFAIvr__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=WaoAAM3s__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=70kYAMLt__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=8ZUEAFLu__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=fAcCASLv__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=wzCCAODv__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=wkAAAOTw__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=Dap_AJzx__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=gxwrABLy__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=we4fAITy__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=VHB4AFTz__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=zX94ACv0__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=FAR1AND0__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=WUu3AAz1__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=Z8svALD1__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=xFUDAEX2__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=284DAJn2__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=KhQqANf2__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=WQi7AGP3__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=pr8CAPD3__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=Y_QAACX4__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=t9C9AIr4__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=aQsDALP4__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=j6EdAOz4__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=j9EgATH5__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=b4wVAHL5__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=e3h4Adz5__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=5NlNAAv6__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=0_CmAD_6__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=X2wBAH76__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=IboJAbP6__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=8ijAAO36__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=pv4TACD7__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=hYaVATf7__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=e5NRAGH7__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=BYsIAID7__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=AKcNAb77__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=Bq0IAPH7__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=AAEeAA_8__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=btxSASj8__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=oVYWAEj8__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=LV6CAHH8__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=ufmNAIb8__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=H_UpAKD8__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=g51ZALz8__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=qYICANT8__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=3M8GAPL8__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=POYLABP9__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=Jc4EAC79__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=8y5AAEL9__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=bM-lAFv9__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=W79_AG_9__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=HDgXAJH9__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=KR-LALP9__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=PokMAL39__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=H1IfAdT9__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=kYJmAOT9__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=V_xZAO39__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1331960595593680101&after_author=wU6lAP_9__8J&astart=840',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nVrije University of Amsterdam done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    vrije_uni_amsterdam()