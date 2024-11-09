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

u_name = "Ghent University"
country = "Belgium"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def ghent_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=H6J_AA7w_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=O5dkAF9O__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=Xy0dAAVm__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=QfKDABWA__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=cYsIAGiO__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=-vwrAByX__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=TXACAMCf__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=0SQeAOyr__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=zR0EAPq1__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=2f9_AOG7__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=cb4cAAPA__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=WysdADbE__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=lNogAMXG__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=CDUEALbK__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=wRIZABfM__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=EoIXAAvO__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=k0QLAO7Q__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=dUYyAfLS__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=GRIOAL7U__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=dij9AHfX__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=DCxyAUXZ__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=TcQNAMHb__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=ntl7AJ7d__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=wbgCAAXf__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=Kz0OANLg__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=6IrzAAni__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=Ccg-ANni__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=0Ji-ANvj__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=9OtGALvk__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=sV1WABHm__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=LrWCACnn__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=-H4JAObn__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=gDYCAL3o__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=XowPAKfp__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=UKwEAHHq__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=2Hk5AEbr__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=PrcEAEHs__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=mX4dAEXt__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=ux4vAOrt__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=vK0CAKbu__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=CrknACPv__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=7nQfANrv__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=YEBdAK3w__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=CCAEAJXx__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=57o2ABfy__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=HTAFALby__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=ea4rARLz__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=O2xVAHPz__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=dQSzAAH0__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=AzdnALr0__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=PscQADL1__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=js0nAHn1__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=f7oCAMT1__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=PYkGAB32__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=wv0RAHf2__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=mH6zANH2__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=OmieACb3__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=_mMAAGz3__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=J9h-ALn3__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=9MooAPb3__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=xIQhARr4__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=e7UyAFr4__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=TlciAJX4__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=KwI8AMj4__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=ybjCAPj4__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=hPwUASH5__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=soHsAE_5__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=aFMyAGT5__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=iYIsAX35__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=F1hWAJ35__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=orMRALL5__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=EElTAOz5__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=Lx4hABT6__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=Ach7ADz6__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=5glDAV36__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=4DAAAHv6__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=dwZPAJb6__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=TloSALT6__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=RZ3JAMX6__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=vBpNAen6__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=8zA5AQT7__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=wofCACj7__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=mPpiAFr7__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=nkLsAHH7__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=xoBkAIz7__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=DawMAKb7__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=GPWZAMX7__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=i0oBAd_7__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=WMUAAPT7__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=jIUTAAP8__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=EsuQACP8__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=pXmSAC_8__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=3IeNAFj8__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=eucQAHr8__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=kFa4AIv8__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=ElFVAKD8__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=v81KALL8__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=os2mAMj8__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=vqZ6AOD8__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=7zMAAPj8__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=VpT0AAn9__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=hM7XAB79__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=-BHOAC_9__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=r00bATr9__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=RFmNAUn9__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=RPoHAF79__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=uA6nAGj9__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=xEkeAHT9__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=9sWMAH39__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=RCp9AIj9__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=yHaGAJL9__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=RsAeAaH9__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=bjgAALD9__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=1DlrALz9__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=ajJyAMn9__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=60GZANP9__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=0QSRANz9__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=Y0tUAOr9__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=d4ryAPH9__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=1737661253683975619&after_author=ysMZAAL-__8J&astart=1200',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nGhent University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    ghent_uni()