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

u_name = "Monash University"
country = "Australia"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def monash_uni():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=j1aNAIZU_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=SYEBANyn_v8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=L_dFADPu_v8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=BDWYALMz__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=_vnYALNQ__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=1L0QAENl__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=InAAANFv__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=KNVRAOt8__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=mc0GAIiJ__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=sB0AAJCQ__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=lcp1ACOW__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=VzNPAMyb__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=KjWaAP6h__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=j8wAAXOm__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=FHU8AVqt__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=3ia4AP2w__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=eXxWAJm1__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=J-wHADa6__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=IDLIADm-__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=e1gJANPB__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=EBEHAPzE__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=k1A6AKTG__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=AtJDAJnH__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=NWcCAAjJ__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=AZJpAPTK__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ie8yAEfM__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=4DswAI7N__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=jxcWAL7O__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=PMQgAJHQ__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=wSi9ADzR__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=AhkAAO_S__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=2IkJAIbU__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=0h-EAJ7V__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=sckLAN7W__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=8OGUAJfX__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=uhcIAIHY__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=hlIsABPZ__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=5eZ5ANLZ__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=YkEpAOXa__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=Z8wzAN7b__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=w1UyAH3c__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=zl5mAULd__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=xyUcABre__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=7CmYAAHf__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=PN4qAIHf__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=-p61AE_g__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=E_clAMjg__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=0NaJAE_h__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ylTyAL7h__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=_LdRAJ7i__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=RyiYAPvi__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=3HgWAI_j__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=dYIDABzk__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=Lmj4AGDk__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=UecdANvk__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=rwxnAI3l__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=08iYAA_m__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=yK6aAErm__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=DIRaAB_n__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=xuRHAWbn__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ZN1-APLn__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=prAUAGPo__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=MGERAPTo__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=nwRKACTp__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=bHUcAIXp__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=YkU3ALzp__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=xzUdAEbq__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=MwxmALfq__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=tC-zADHr__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=AcSOAJXr__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=By0JABrs__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=xPgtAGvs__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=wc56ALHs__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=yFUjAPfs__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=-cwIAFft__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=rkeZAL7t__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=1jy-ADzu__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=NjHhALXu__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=MLdNAPbu__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=k-B3ACfv__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=3BQEAFjv__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=LA7HAJrv__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=67JkAPfv__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=J4NxACXw__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=nyqRAV3w__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=uYsBAIDw__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=XOYCAKfw__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=d4kCAOfw__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=VhEGADTx__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=aQMGAFjx__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=XbGaAH7x__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ktCYAMLx__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=Kp0IAPTx__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=TvdwACry__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=SLXCAFDy__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=z_SAAGjy__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=luIIALPy__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=9v5QANLy__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=GPOQAPzy__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=93vqACnz__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=1UcPAGrz__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=wKyQAJDz__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=bA-FAJ_z__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=Bz8jAL_z__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=wScMAd_z__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=n4ZTAAv0__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=3XSfAFL0__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=RDmDAH_0__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=BSXKALH0__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=BOSoANL0__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=jDG7AeX0__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=4g_pAAD1__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=FoJRAS31__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=z0kDAFT1__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=xCeYAHz1__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=QYwgAJn1__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=S1wDAMb1__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=AzowAOz1__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=OJKEAP71__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=1TvyABf2__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ZBgmADb2__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=YvowAF_2__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=KSd8AIH2__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=E04aAJH2__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=WEh4ALH2__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=74MBAen2__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=8mopABb3__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=QoB5ADv3__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=lvAMAFr3__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=xP0lAHX3__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=j6muAIv3__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=aqwCAJf3__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=g30FALX3__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=l1IhAcT3__8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=WvYHANj3__8J&astart=1350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=QVkmAPr3__8J&astart=1360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=txmfABD4__8J&astart=1370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=o5Q3ACv4__8J&astart=1380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ddUrAUb4__8J&astart=1390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=q4GhAF74__8J&astart=1400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=K1X2AHX4__8J&astart=1410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=u5FsAIb4__8J&astart=1420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=KuEAAJz4__8J&astart=1430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=659hAK_4__8J&astart=1440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=fMkeAMj4__8J&astart=1450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ubMHAN_4__8J&astart=1460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=kVE7AAD5__8J&astart=1470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=RLM8ABb5__8J&astart=1480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=32wBAC75__8J&astart=1490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=-gtHADb5__8J&astart=1500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=cTrXAED5__8J&astart=1510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=HKKXAFX5__8J&astart=1520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=gffvAG_5__8J&astart=1530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=hy8wAYP5__8J&astart=1540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=q5mIAI_5__8J&astart=1550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=2GZ9AKD5__8J&astart=1560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=w8EDAKz5__8J&astart=1570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=DPIdAMD5__8J&astart=1580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=vVtmAMr5__8J&astart=1590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=SUOYANv5__8J&astart=1600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=kRkPAO35__8J&astart=1610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=clHoAAH6__8J&astart=1620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=lr9bAAn6__8J&astart=1630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=QEC1ABj6__8J&astart=1640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=vycRACX6__8J&astart=1650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=BZ9pADn6__8J&astart=1660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=aXOWAFr6__8J&astart=1670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=_2s0AG36__8J&astart=1680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=LVwmAXr6__8J&astart=1690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ksjFAY36__8J&astart=1700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=RH4tAKH6__8J&astart=1710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=F7BNALP6__8J&astart=1720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=d6DcAML6__8J&astart=1730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=38QqAM_6__8J&astart=1740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=DCQGANv6__8J&astart=1750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=uNgOAOP6__8J&astart=1760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=gtMvAOz6__8J&astart=1770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=MCYjAP76__8J&astart=1780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=R4cHAQf7__8J&astart=1790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=z7sBABj7__8J&astart=1800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=O-khACb7__8J&astart=1810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=BcMSADf7__8J&astart=1820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=0BCeAET7__8J&astart=1830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=p2hlAVD7__8J&astart=1840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=PuEGAF37__8J&astart=1850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=hZoMAW77__8J&astart=1860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=KUKYAHn7__8J&astart=1870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=UjyZAIH7__8J&astart=1880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=-_lnAIn7__8J&astart=1890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=ZXFkAJD7__8J&astart=1900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=sVBrAJn7__8J&astart=1910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=mvkgAKb7__8J&astart=1920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=zcAxAbX7__8J&astart=1930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=4C6ZALv7__8J&astart=1940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=J0ETAMf7__8J&astart=1950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=DkfRANL7__8J&astart=1960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=3918598370877205258&after_author=XNUvAOD7__8J&astart=1970',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nMonash University done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    monash_uni()