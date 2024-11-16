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

u_name = "University of Colorado, Boulder"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_colorado_boulder():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=JRIMAIux_v8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=1vMEACcT__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=kU0hABFK__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=9EhPAE1T__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=5RVIASJp__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=Tg4uAEh7__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=tJsDAPiJ__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=iIojANaU__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=rwCLAMye__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=ZVNuAOSm__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=Ph4LAEOr__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=SnxeAMqt__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=MdwgAMK0__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=YqcCALK5__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=999QAP-8__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=limOAD_A__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=DJU1AdTC__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=5PQNAOXE__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=GvpDAS7J__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=iMQJANrK__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=tlpNAH_M__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=ivEQAJXO__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=b6PcAEXQ__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=OO0yAI_S__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=wr97AIvT__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=VD3pAOjU__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=L4mcAPbW__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=FmECAD7Y__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=KggzAMHa__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=k_gEAOzb__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=0qQ1Afvd__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=OF4IAK7e__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=9jD4AJLf__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=cqgBAKvg__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=CE9aADnh__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=ZpoyAQPi__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=ch4bAG_i__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=afoAAHfj__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=YVUDAE7k__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=8jdmAVfl__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=pjcLAcPl__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=GFqRAPfm__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=HNIsAJzn__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=VxYFAGPo__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=hNCxACfp__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=y9VtAR7q__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=lQIAAYvq__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=8vyNAOXq__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=zxHPAHDr__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=UyEGAEDs__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=47UcAK3s__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=fWfAAF_t__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=RdiqAdvt__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=Z6D8ADHu__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=ReKcAa3u__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=WU7nAEnv__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=w02kAJDv__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=LE4WABXw__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=vJVFAHLw__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=yi0nAeXw__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=XolKAF7x__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=dCUMAIzx__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=4DdsAMfx__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=6kdRABvy__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=lkCeAG3y__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=cLgCAKjy__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=UK5HAADz__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=LpuSAHzz__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=JeAGAMnz__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=UyCEAQj0__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=rxlhAUb0__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=txQWAHv0__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=4y17AML0__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=mRTjABL1__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=h0AKAHD1__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=lovHAMz1__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=aToEAB32__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=Wd4OAFD2__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=xJ_2AKP2__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=gq9KAM72__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=McgOAAH3__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=oZQnADz3__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=FZRVAH33__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=hTxMAaf3__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=UYHMAMf3__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=VMSLAOz3__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=sd8PACH4__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=KMV1AGv4__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=Up3SAMD4__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=GJunAPj4__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=d1BRARP5__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=XEMhAD_5__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=xS2oAFv5__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=_K2wAYv5__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=qnh_AKj5__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=Ux9bAOf5__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=vC6OAfz5__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=RTAJACT6__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=r6IOAE76__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=5R2BAHT6__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=2Kx1AY_6__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=KB-7AbP6__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=1PHlAMz6__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=4hFJAe36__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=F36XABH7__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=ROwAACT7__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=GQEhADv7__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=UUcCAFD7__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=-xlyAHT7__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=IR0oAJb7__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=tacxAK77__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=tt6WAMT7__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=blMxANn7__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=SJ0eAfr7__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=bia3AB78__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=JiRJADr8__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=v4UMAEr8__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=EEYmAH_8__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=GsBIAJb8__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=gOXgALn8__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=9gTtAMz8__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=1LzdAOH8__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=FfDPAPb8__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=KAtGARD9__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=u--dABz9__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=kjZLACr9__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=wHrDADz9__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=vxtOAU_9__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=sTw5AFv9__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=b7zlAGT9__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=cpI7AG39__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=5cINAHr9__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=nZQAAIz9__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=LFpPAZr9__8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=-miEAKj9__8J&astart=1350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=z3X-ALD9__8J&astart=1360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=QcNTALb9__8J&astart=1370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=wYpOAL39__8J&astart=1380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=kpUAAMf9__8J&astart=1390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=WrnbAND9__8J&astart=1400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=g-iJANf9__8J&astart=1410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=ulvVAOP9__8J&astart=1420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=wCkaAez9__8J&astart=1430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=HQtqAPv9__8J&astart=1440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=10680603084482565841&after_author=sbvZAAn-__8J&astart=1450',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Colorado, Boulder done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    uni_colorado_boulder()