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

u_name = "University College Dublin"
country = "Ireland"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_college_dublin():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=18013644464360602948",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=jygPAMhq__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=lL8CAKiX__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=gb6-ADGu__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=X9AuAMO3__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=p6S6AI_B__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=3QXmAKTJ__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=S5k3AKLP__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=TQ9uAa7U__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=dS0dAHTX__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=k7bUADjb__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=9EdNAMnc__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=upaoAGje__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=1UIzAE7g__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=PCMFAGzi__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=MCNSAJ3k__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=5SpDALPm__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=QdK4AGHn__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=OhIAAAfp__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=DVDyAKfp__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=_kNaAKbq__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=9GCDAGzr__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=zB4uAAXs__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=S8YNAOPs__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=7YsAAMjt__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=1oo5ALbu__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=pJNIAEPv__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=MFB5AL7v__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=mkQkAIHw__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=8UQBAEvx__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=yVkbANvx__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=uTomAIPy__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=Su8PAPXy__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=vkIdAE_z__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=hHARANzz__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=eSAFAC30__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=I-IIAJL0__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=YE0EADn1__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=0WkcAHv1__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=bSCGAP_1__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=5BQoACT2__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=UrEoAFz2__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=ZPoAAMX2__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=AdipABX3__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=v5WcAHT3__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=DF0pAcn3__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=WXARAP73__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=xRcBATn4__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=GpJLAGX4__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=BGi5AJ74__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=0yocAMz4__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=tsVhACH5__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=WH55AG_5__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=n2EaAJT5__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=AcITAMX5__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=KFa_AOj5__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=JzA6ACH6__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=9M-RAE36__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=A9g8AW36__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=MRjrAIf6__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=qg4lAK_6__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=-kn0APz6__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=KlGbACL7__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=pO5BAEj7__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=ta8IAWv7__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=BCSzAJL7__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=866iALL7__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=IAY3AeH7__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=Oa2DAfv7__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=g3YSAAz8__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=EFskACv8__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=nTuQAEr8__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=aKpIAFz8__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=AuUmAW_8__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=lgYDAIX8__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=gtjxAJn8__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=a2MlAKz8__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=P366ALn8__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=ulLgANH8__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=kocqAOn8__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=oTflAPz8__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=74GiABH9__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=5zqtACv9__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=HyFPAE39__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=U6OTAFj9__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=OBn5AGn9__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=qfvoAIT9__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=pE1BAJj9__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=w8SBALL9__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=VVZZAMD9__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=yI4zAMz9__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=u_1yAN_9__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=18013644464360602948&after_author=1gk_Aef9__8J&astart=920',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity College Dublin done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    uni_college_dublin()