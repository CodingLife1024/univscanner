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

u_name = "RMIT University"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def rmit_uni():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=R4sBAE-A__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=ukKiAXKm__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=skisAEO0__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=DuIXANu___8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=e1kTAJ_I__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=8ygVACHO__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=q4kkAObS__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=nQkVAHbW__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=Q08lAM7Z__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=YeEJACzc__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=kWsLAU_f__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=qY5AABvh__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=UhgQAJri__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=SBgVAPDj__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=WUgEAADl__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=GOxXAAbm__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=ONA6APvm__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=CeYRAM_o__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=tJh0AY_q__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=0JklACvr__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=GeSPADfs__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=jfMKANPs__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=oZy-AHDt__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=1wEUACvu__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=_t-HAGPu__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=vaKxAOLu__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=d-8BAJjv__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=5IFMACXw__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=aKp-AMfw__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=o12RAC7x__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=-c0AAOrx__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=ImRaADDy__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=c76FAJry__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=QuSUAOHy__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=7x5OADPz__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=jmwBAMPz__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=zFCWAAf0__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=qjsrAH30__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=VApoAer0__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=2Cx3ADv1__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=cSxfAYH1__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=j--TALb1__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=AuEQAOj1__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=1LsWAEf2__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=Jf8MAHv2__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=XUtqAfH2__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=wRIKAGb3__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=I_IoAJv3__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=zE8UAOH3__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=M7kMABz4__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=zasDAEn4__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=jT0pAH34__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=KH1hANT4__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=6Rq2ABz5__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=yfMKAF35__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=GcUuAIT5__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=AMYpAK35__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=v91iANr5__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=5VMjAf75__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=RsyGACj6__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=viAOAFX6__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=K94AAHX6__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=SWKAALj6__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=lE8WAeX6__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=zbQZAAj7__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=mjWpADP7__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=38U-AFn7__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=tnsLAXH7__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=UtytAIr7__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=K_DAAKT7__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=j_GBAMX7__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=XenKAeP7__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=k3XVAAb8__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=133vABv8__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=Mqn-AC78__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=w8kJAD_8__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=zy2GAFD8__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=OiJqAHb8__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=HUQKAJL8__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=inEZAKj8__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=IQdAAMT8__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=NAc5AdL8__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=0RcCAOX8__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=eZPGAPf8__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=nboPAAf9__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=zvYfACb9__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=oRkPAED9__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=UiIEAFP9__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=Gva_AXD9__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=YdsAAIL9__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=qTELAJr9__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=f8WKAKz9__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=Y-ePAMj9__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=j0YlANH9__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=8JoAAOL9__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=UIPMAO_9__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=8943956419179841881&after_author=rBiXAAX-__8J&astart=970',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nRMIT University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    rmit_uni()