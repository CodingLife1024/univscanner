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

u_name = "Stockholm University"
country = "Sweden"

all_faculty_stockholm_uni = []

def get_faculty_data(link, headers):
    global all_faculty_stockholm_uni
    all_faculty_stockholm_uni += search_faculty_list(link, headers, u_name, country)[0]

def stockholm_uni():
    global all_faculty_stockholm_uni
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=DL8NAFZU__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=WDEPANqM__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=pZiNAGyk__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=q5gPAFey__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=LfZLAEa5__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=aPsDAEbD__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=7VIuAdHJ__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=IPE7AA3N__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=RG8NAZjQ__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=_QkeAHzU__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=DX4GADLY__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=SBsuAKfa__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=Dws6ANnc__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=WdUUABzf__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=rdsFAF_g__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=6N-GALTh__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=kT0OAAHk__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=B8gDAA7l__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=JtF_ANLm__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=DZ4zAJLo__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=yNdqAI3p__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=Ar6BACTr__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=K78CADXs__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=DEwLAB_t__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=RZB9ABPu__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=tT8CAObu__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=QYuZAJXv__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=mHMNAEXw__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=bYk9AaLw__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=l1QeADHx__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=kEDpACjy__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=pY4KAKDy__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=TkBsAGXz__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=Qzl6AAr0__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=zgj-AJb0__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=RasPABT1__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=BatLAX_1__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=xtOEAdH1__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=QMNzAA72__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=sFskAGH2__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=fyExAa72__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=cn61Aen2__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=I7t-ACr3__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=NPUqAGb3__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=lhAGAKf3__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=oyh6AML3__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=Fz1rABH4__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=8Fx5ADf4__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=xvI_AHT4__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=cOEVAM74__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=WUmaABf5__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=PJ0_AE35__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=DtAzAH35__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=otVYALL5__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=fs-BAM_5__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=N1piAPP5__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=MC94ACb6__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=XZTQAGn6__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=qJ3SAIz6__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=re7OALr6__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=ofp8AOv6__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=NJ9fACL7__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=8ucNADz7__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=8RUQAWX7__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=V5X4AJT7__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=CIk8Abj7__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=OR2YANv7__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=CT0GAPH7__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=hdMfAAf8__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=AAMuACT8__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=C0QNAE78__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=9glXAGT8__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=aU9LAX_8__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=kgi0AKr8__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=epunAMn8__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=nkuiAPL8__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=qq8tABP9__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=BUsbADL9__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=xDj2AFL9__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=LPf2AGD9__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=yrUbAIT9__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=AEOVAJX9__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=uwFGAKL9__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=PFUKALf9__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=-Z2RANH9__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=0hIMAeX9__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=xhwyAPT9__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8484286818777024965&after_author=7lArAAT-__8J&astart=880',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nStockholm University done...\n")
    all_faculty_stockholm_uni = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_stockholm_uni)]
    return all_faculty_stockholm_uni

if __name__ == "__main__":
    stockholm_uni()