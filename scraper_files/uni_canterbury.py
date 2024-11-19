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

u_name = "University of Canterbury"
country = "New Zealand"

all_faculty_uni_canterbury = []

def get_faculty_data(link, headers):
    global all_faculty_uni_canterbury
    all_faculty_uni_canterbury += search_faculty_list(link, headers, u_name, country)[0]

def uni_canterbury():
    global all_faculty_uni_canterbury
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=119869554344774657",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=CPnVAGq-__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=qIAGAMrL__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=silpAOnY__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=PD0tAKXf__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=NKkPAO3j__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=aOuXACXo__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=UsptABbq__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=tLqFAELr__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=EksAAIvs__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=WMwOAWPu__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=DR0WADLw__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=yu0CAGbx__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=kkFeAF_y__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=N4kFAIXz__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=fckDAEL0__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=oqkGAPv0__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=-LQKAGP1__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=mRgCAIb2__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=ddM-ACr3__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=_ocVAAb4__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=j-6FAIb4__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=B0oaABD5__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=3j6UAJ_5__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=VFUxABL6__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=BooAAHj6__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=L_xwALD6__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=IN-ZADj7__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=jSNXAIP7__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=gdYIAMT7__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=qkaZAOj7__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=6YKAAA78__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=nQkxAGH8__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=rCYAAJ_8__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=o_ABAPf8__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=yb4GAR39__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=SvAgADj9__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=vqg0AHT9__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=6v6UAJr9__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=--CZAMn9__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=BrSdAOv9__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=7IuUAP79__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=885oACX-__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=zJ3MAD7-__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=dl6DAE3-__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=CN4VAWL-__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=GwuIAHH-__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=b5wGAYj-__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=GtyqAJX-__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=iOsbAKT-__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=RdjbALz-__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=J_ZNAdL-__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=sdUHAOL-__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=hRMUAPX-__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=etx-AAn___8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=FSO0ARr___8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=uWIAACX___8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=L5V1AC____8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=J1CUAD7___8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=sOvaAEz___8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=qeMBAF3___8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=txPFAGr___8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=l-GuAHX___8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=RQ8nAYD___8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=AMrcAIn___8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=iuhOAZP___8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=JnoWAJf___8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=oJmfAKH___8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=YlpUAab___8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=4soAAa7___8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=KjJ8AbX___8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=6deLALr___8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=va8hAb3___8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=peooAcP___8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=OK9NAcb___8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=6gn2AMr___8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=zCKEAMz___8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=EW6BANP___8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=G9HCANj___8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=vtJ_Adv___8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=ErXeAOD___8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=-WC1AeL___8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=K_qoAeX___8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=B25PAOj___8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=wSKVAer___8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=njpfAO3___8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=zF5OAe____8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=20wfAfH___8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=9KimAfL___8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=SXt1AfP___8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=KxhqAfT___8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=FBFWAfX___8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=MGWjAfb___8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=46LRAff___8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=POLKAfj___8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=mvw2APr___8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=DuPAAfr___8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=5zyZAfv___8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=JP7HAfv___8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=KCJKAfz___8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=119869554344774657&after_author=fUi0Afz___8J&astart=1000',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Canterbury done...\n")
    all_faculty_uni_canterbury = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_canterbury)]
    return all_faculty_uni_canterbury

if __name__ == "__main__":
    uni_canterbury()