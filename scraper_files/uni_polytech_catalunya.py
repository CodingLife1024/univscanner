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

u_name = "Universitat Politècnica de Catalunya"
country = "Spain"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_polytech_catalunya():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=rbg-AIaz__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=u8ACABnG__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=JRKCAPHN__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=5GcaAALV__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=PcEPACrZ__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=lHkBAAHe__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=bIIRAO3h__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=4wovAKzj__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=S_oTAKbk__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=f2dGAHzm__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=Y5R-AfLn__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=x6IBAEjp__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=NNICANTq__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=H9sjAIPr__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=AKEcAU_t__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=0gaHABDu__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=6iAiALDu__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=iixEAR3v__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=6BcXAcnv__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=Ui8UAETw__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=oSEKANbw__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=caI3AFHx__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=WmgOAODx__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=NVRaAEDy__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=1-vIAL3y__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=U9sCAP7y__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=ZiGSAUHz__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=DwcEAObz__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=gNsXAH70__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=bMgCANL0__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=8VOWAC71__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=BVQWAHz1__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=59YwAe71__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=qqgFAA72__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=2dYaAF72__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=5UwdAJH2__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=Ko0KAKf2__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=d1RdAOb2__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=fsUSACL3__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=qNe-AHP3__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=c85wAbn3__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=pcF2AAn4__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=g0MaASb4__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=LAkQAHH4__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=WMkIALL4__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=NSxlANX4__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=tVplAAP5__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=MdWWATb5__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=LNSWAHr5__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=3PGWAKr5__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=zetnANb5__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=aMBHAOr5__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=2Z4OAAz6__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=TxNpATT6__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=PX5HAGH6__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=-FkfAHP6__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=2_oWAIv6__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=8spKAcv6__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=V14bAOT6__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=_GJHABf7__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=r1u3AS77__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=RzRuAEb7__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=YDOWAFj7__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=IwPyAIL7__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=YHACAJn7__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=pjcnAK77__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=I9kkAMj7__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=V0sgAOv7__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=M4BHAP77__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=TecrABr8__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=urccASf8__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=1FqEAE38__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=UINoAIH8__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=qtRkAJ38__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=SJQuALD8__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=5sZ_AMn8__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=iFeWAOH8__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=SlUVAPX8__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=t-OIAA39__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=x7nNARv9__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=C0MiADP9__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=zQBDAD79__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=0fZ5AEr9__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=nEABAGD9__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=wPU2AXL9__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=Nl25AIn9__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=0CxLAJz9__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=mwB6ALD9__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=gutDAcH9__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=BBDNAdj9__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=g_hHAOf9__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=VCpVAPX9__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15919159503148751864&after_author=KjARAAX-__8J&astart=930',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversitat Politècnica de Catalunya done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    uni_polytech_catalunya()