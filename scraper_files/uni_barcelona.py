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

u_name = "University of Barcelona"
country = "Spain"

all_faculty_uni_barcelona = []

def get_faculty_data(link, headers):
    global all_faculty_uni_barcelona
    all_faculty_uni_barcelona += search_faculty_list(link, headers, u_name, country)[0]

def uni_barcelona():
    global all_faculty_uni_barcelona
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=i7d7AFsJ__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=H1gKABp1__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=M9UpACSQ__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=4Hd1AMih__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=iSqHADaw__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=PDMmAAG3__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=cEzHAD3B__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=B8PTAAzH__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=DpYHACjK__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=giRoAOnN__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=rZ4_AMHQ__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=j5DTANXT__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=8utGAADV__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=bZkMAETX__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=leVjAMDZ__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=Bv-VABPb__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=isbnAPrd__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=JdUpAHjf__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=l9uQAMHg__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=fRJ-Adjh__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=s2ulARPj__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=iHWbAOHj__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=yMTGACnl__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=wCG0AJHl__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=-Hw8AOnm__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=s_V5AIrn__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=6gw3AGfo__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=1SYkAFLp__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=pFJnAATq__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=2LpDAHrq__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=UAq3AG7r__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=U9slAPvr__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=NmdJAZbs__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=ycZFABnt__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=5JxQAePt__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=DPp8AILu__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=JY8KAOfu__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=8C4UAGbv__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=XwU2AKfv__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=9_GoABbw__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=kyR1AFfw__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=YDJHALzw__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=A49wARHx__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=Dx_RAK_x__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=6nNrATTy__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=skq1AILy__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=HDp5AM3y__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=chMGAC_z__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=BlU6AGjz__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=tLRMAJnz__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=t39PAN7z__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=eRMxACT0__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=u28BAHL0__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=9lwSAcf0__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=6K4gABb1__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=1YJnAF_1__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=RY8xAYP1__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=2BvRALv1__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=xQH6APT1__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=Y6aVACb2__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=39aBAEX2__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=ubgpAG_2__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=fC69AJf2__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=wcqZALn2__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=3n5nANj2__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=u6VGAAL3__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=3NaBADD3__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=2nh9AEX3__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=i_5IAWL3__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=odi_AKL3__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=YFnPANP3__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=xRglAPr3__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=9AoHACb4__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=kjbnAE_4__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=hIZqAWz4__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=ZXgYAHj4__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=W6cMALT4__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=JRGoAN_4__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=ilA9AP74__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=7a2NAB75__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=teOpADr5__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=m5btAFb5__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=7fDQAHz5__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=gWKNAKH5__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=Ee31ANP5__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=fnV_AAL6__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=rzHJACb6__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=eR6WAFP6__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=m-kHAIP6__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=QRBUAJ36__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=vpnRAK_6__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=fwcqAMj6__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=rCs3ANz6__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=lYFGAPr6__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=YG5JAQ37__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=w1C5ACj7__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=b4OqAFL7__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=yhCBAGz7__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=OaeWAIb7__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=GsNRAKP7__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=HX0VALf7__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=v8_LAMX7__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=vfRGAN37__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=VOOVAPz7__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=tKIiAAj8__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=t0UfACH8__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=yp0IAEH8__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=TBheAE78__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=csIrAGz8__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=C1UZAXr8__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=VASKAJr8__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=UvoJALP8__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=JrwTAMX8__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=yXR1ANz8__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=gTUAAPX8__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=g1wsAQf9__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=SV-WABL9__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=lbtIACf9__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=6JlMATr9__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=tKsEAEf9__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=nhFIAVP9__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=rzTHAGL9__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=J-RlAXH9__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=OQ4eAIL9__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=ofOGAJf9__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=c-irAKL9__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=iBMbAK79__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=LZehAbv9__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=YpuWAMb9__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=HGpoAM79__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=cKE7AOX9__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=JbNnAPH9__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=Hm9jAPv9__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=15918451262755526508&after_author=SIUVAQf-__8J&astart=1340',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Barcelona done...\n")
    all_faculty_uni_barcelona = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_barcelona)]
    return all_faculty_uni_barcelona

if __name__ == "__main__":
    uni_barcelona()