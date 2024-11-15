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

u_name = "Seoul National University"
country = "South Korea"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def seoul_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=0G-LAN3g_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=zMcZAIRC__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=45uvAPpw__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=PMkCACqG__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=kOXOACGU__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=tYw3Ae6a__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=CxBiASqm__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=7WUmAfSs__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=myUNAF60__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=-LUBAF23__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=KFlJARW6__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=D8ciAae9__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=TFhpAMy___8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=fm2XAGbD__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=GjoGADHG__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=-bgvAHbJ__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=IvR8ATPL__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=I_yWAMHM__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=nbEeAFHO__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=45otAK3P__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=tT3jAD_Q__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=IkgNAJzR__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=s1cQAPTS__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=t5oDAZDU__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=gfR8AGLW__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=WIUZAPzX__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=hKdsALvY__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=T42pALXa__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=8c5ZALPb__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=XTkJAFPd__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=Os4CAFre__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=JMlVAP7e__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=M6yMABzg__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=WzdcAODg__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=eBwAAJfh__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=43aMAFHi__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=uUyIAAPj__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=9g88AKDj__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=pOkiAGPk__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=-QwUAOrk__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=qRZyAIPl__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=hTeyAGfm__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=1VUdABrn__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=lF06AGzn__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=9Y2FAcDn__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=QdoBALPo__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=t7ePAC7p__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=h-VhAJrp__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=cyuUAN7p__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=fa0KAI_q__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=FzufAAzr__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=LGI9AGjr__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=BRQEAOnr__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=wJFmAH3s__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=uiLYAMzs__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=HmjeABLt__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=ep7uAKbt__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=BKtaADvu__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=iRRJAZDu__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=hz8TASTv__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=kVEPAIrv__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=B8AXAPrv__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=hRi9AH_w__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=U-iZAMDw__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=Vko6ABjx__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=X4oZAEvx__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=FZktAIHx__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=aKQLAMbx__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=Fe_MAA7y__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=AaVBAZPy__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=zSQSAeDy__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=e3cxACbz__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=LEihAXPz__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=RHGLAKvz__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=JtqDAAj0__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=ktUqAUv0__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=97TMAHH0__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=APIOAcH0__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=elijAAj1__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=qmGtADT1__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=EpQQAYX1__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=ePoCAMD1__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=0kwyABX2__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=eQZhAFn2__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=IVxqAJP2__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=R9WKANv2__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=tFqMADb3__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=UcbsAIz3__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=2ycFAMr3__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=FXKLAAf4__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=RbgkASX4__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=dHiPAEv4__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=_KMiAXf4__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=YjmBALH4__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=qWV0AM34__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=mcftAOn4__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=PA7cAP_4__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=3IT8ADj5__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=Sz0ZAFr5__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=HsEkAZP5__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=BH5BAK35__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=HoaDAMX5__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=OYxWAe75__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=CpdtARv6__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=WkTGADf6__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=_Sr1AE36__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=H4r2AGv6__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=j90rAIb6__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=B-tkAKf6__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=0tiYAMD6__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=ygopANr6__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=euIpAPf6__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=dmYDAAn7__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=QcvDACb7__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=sxpVATX7__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=of3qAEv7__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=Tw1PAFn7__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=2bhDAGj7__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=oZp_AIf7__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=sP0IAaL7__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=NpXoALf7__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=Ejk0AM_7__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=1fqcAOT7__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=KRXTAPv7__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=plH-AAf8__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=9132855923674982206&after_author=JdSnABX8__8J&astart=1260',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nSeoul National University done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    seoul_uni()