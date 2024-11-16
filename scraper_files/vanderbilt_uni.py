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

u_name = "Vanderbilt University"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def vanderbilt_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=ovQMABl0_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=UmSmAIwA__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=CdMJANAt__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=A937AKVY__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=OCueAPNw__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=qHkBAO96__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=lOwAAHeM__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=v5iYAfKX__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=NciGAKef__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=3nAUAAKo__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=tR4OACuv__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=VAi6AIay__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=r3IYAF63__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=gUwAAGe7__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=3f5AAGG9__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=_RN8AEjB__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=B196AKfD__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=hYwAADXG__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=YagOAM7H__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=FwJ2AEzK__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=-AQCAO3L__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=gmkbAILO__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=coUZAPTP__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=VsIFAHnS__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=hC4BAK3T__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=9nQsAPPW__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=1GQ5AOzY__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=CxkYADja__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=tPO6AU7b__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=71FCAa7c__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=0DkzAXnd__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=m8Z8AK_e__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=JPE1AOff__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Rkt0AIvg__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=7n1qAL7h__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=wmsrAIXi__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=ANPMACDj__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=BWEPANDj__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=aolPARnl__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=-as-ABfn__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=030SAGXo__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=HUoeAELp__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=m0u0AP_p__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=l7nBALLq__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=tSkPAGrr__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=2IR6AC7s__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=2tdQAMPs__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=3JpMAFDt__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=5asKABHu__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=7ykGAGvu__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=YQd2AA3v__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=XHgLAHjv__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=C1MEANLv__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=6cgMAGPw__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=FgJ_APvw__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=6MQ_AGrx__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Og9yAPnx__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=DpaOAEzy__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=7NEhANTy__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=C3s_AF3z__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=N9I9ANHz__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=YtIwAC30__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=QdsOAJf0__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=UZc1AOj0__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=0qYtACv1__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=eXUtAHv1__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=onCtAN_1__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=VBTNABv2__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=84kTAI_2__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Cdx2APv2__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=SroKADn3__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=HF_aAGz3__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=KXSvALP3__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=U6WGAQ_4__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=GpNhADf4__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=egYAAGj4__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=0vinAJ34__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=njZYAO_4__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=DU16ACP5__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=ABuvAFv5__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=PzkiAXX5__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=SMsoAYv5__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=AhucANf5__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=ryDGAQz6__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=agZ0AVj6__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=De9lAIL6__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Zh8yAJ36__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=XUYKAMH6__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=7DZAAOP6__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=zhp6Afj6__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=_FO9ACz7__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=kZ18AFD7__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=aRnWAG77__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=X74AAIn7__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=_J1vAKH7__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=gDYKALL7__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=ek4KAcz7__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Z0okAOP7__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=aUIdAAD8__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=jSQvARH8__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=mg18ACf8__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=fgAzAEr8__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=oSxoAWP8__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=GZJkAHD8__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=ioAZAIr8__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=HaF-AKX8__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=6NjyAL_8__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=6OnfANz8__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=IVuBAOn8__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=oaR0AP78__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=3jSLABX9__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=7ytAACv9__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=8mG2ADf9__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Ic02AEb9__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Mz_dAFf9__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=3GwsAGD9__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=EIMRAHf9__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=l8mSAIP9__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=aoWNAYr9__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=8aYvAJ39__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=wbMRAKr9__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=hQEWALb9__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=OLerAMj9__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=EfRfAdb9__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=rErjAOP9__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=SqUIAPD9__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=Y3pVAPz9__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18133135600508121944&after_author=8aD4AAb-__8J&astart=1280',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nVanderbilt University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    vanderbilt_uni()