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

u_name = "Deakin University"
country = "Australia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def deakin_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=Uas6AEcw__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=eEAGACKD__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=gd5KAPSW__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=vBwfAGuu__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=uN0CAN65__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=yaxMAa_B__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=RvgJAFvM__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=b58zAK_S__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=uGRkAAnW__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=uEyDALHX__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=X2EBAarb__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=wCUAAETe__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=-7dUAMTf__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=FoR7ABrh__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=yfMnALXi__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=vwnSAF3k__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=4zOdABzm__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=1a4yAHfn__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=JEOVAFno__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=emgVAMvp__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=YK2zALnq__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=r-DHANzr__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=s-OFALbs__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=G-2AAKLt__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=EQR6ACTu__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=JuwKAAjv__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=dTJ2ALPv__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=GUkDAEPw__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=XJWdAOHw__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=PlU8AHXx__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=BQmRAOPx__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=AeUfAIDy__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=M6OFAODy__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=FJUoAF_z__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=8LtDAMfz__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=nNkWABb0__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=gvkTAGv0__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=D2sVAJH0__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=tCs-AOb0__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=ScdVAB71__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=BywcAXH1__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=MZkVANT1__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=i8uTABr2__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=8GfgAHb2__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=P5wfAdL2__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=rKgIAAn3__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=bYQKAEj3__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=lZoRAIv3__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=IZABAMf3__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=ePe8Afj3__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=MikIACP4__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=_CJrAVT4__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=ceIDAXn4__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=gGA-AKb4__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=_VnAAbz4__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=zIUHANz4__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=Dd4BACP5__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=sgZ7AD75__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=8rdpAGL5__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=DIF4AJL5__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=GN-oAbr5__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=wsxOANT5__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=vaQoAP35__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=R1cFACP6__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=d-49ADv6__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=0IcQAFL6__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=s0eTAGT6__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=8I8uAYL6__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=X9N7AKL6__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=xlVYAL76__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=ZxB5ANv6__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=SDUbAPv6__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=Joo6ABj7__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=7eNnAC77__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=IgfAAFH7__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=koQ8AG_7__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=chMFAIb7__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=Xdz0AKj7__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=T1O6AL_7__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=_lJ8AND7__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=9wcFAOP7__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=vlEYAP_7__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=B4erACb8__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=aOqWADz8__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=VKxiAEr8__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=G4iiAF78__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=bxhEAIf8__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=ERtEAJv8__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=8JZjAK78__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=HmiwAcn8__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=J3gHANz8__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=bAhAAO_8__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=tTeBAP_8__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=4S-XAAv9__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=dpQKACL9__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=EqTxACz9__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=joUuAT_9__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=HZ3eAEr9__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=dSW_AFj9__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=rEVmAGn9__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=dEUZAHr9__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=vLcvAIX9__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=X68xAJf9__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=CbWFAKL9__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=3at9AK_9__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=R1V5ALX9__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=DEgWAcX9__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=9e-AAND9__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=UCqmANf9__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=EX81AOL9__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=dWuxAPL9__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=SCd5AP39__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10412436667236230217&after_author=xNBNAQT-__8J&astart=1130',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nDeakin University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    deakin_uni()