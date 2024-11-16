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

u_name = "University of Campinas"
country = "Brazil"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def unicamp():
    global all_faculty
    links = [
        'https://scholar.google.com/citations?view_op=view_org&org=6300175949274449304',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=e_ZQANeR__8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=8MsFADms__8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=IKEGAOG8__8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=lQlkADHE__8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=ECIGACPK__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=M7AqAAjN__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=akwFAEXQ__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=MgRdAJ7S__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=rXOPADvV__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=dIgFAB_Y__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=HM9uAEba__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=4IwFAJ7c__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=yR_5AHHe__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=poQPAEPf__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=mVAIAOng__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=uhqaACDi__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=SyAIAG_j__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=8j0GACzk__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=XTvcAFTl__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=SwwFAE7m__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=RlBaACvn__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=WjHOAB3o__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=XRo3AN3o__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=ZOSRAL_p__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=OuYFAGTq__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=VWAGAOnq__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=Z6zLAKzr__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=I2C1AArs__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=7sFLAJDs__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=5QyIAefs__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=7hK0AEjt__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=DM4pAJXt__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=QCsSAOvt__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=MpHfAEfu__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=HsrwAMDu__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=hVyvABzv__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=RgvNAJ7v__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=sP85APfv__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=9zALAFLw__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=sZ8SAKPw__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=wgwGANfw__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=IhrhAD3x__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=hYswAJjx__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=LHgSAOXx__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=YmEEABby__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=RJ4aAGzy__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=CHULAcfy__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=ktkFAETz__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=ioBiAHPz__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=aQEGALnz__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=4YYaAAX0__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=_KBGAUr0__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=QX8OAIf0__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=ZdjTAKL0__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=SrYKANX0__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=6A0YAB31__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=2xQJAGv1__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=EWJtAaX1__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=cZq4ALr1__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=egJ9Ae_1__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=GMywACH2__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=lej_AGL2__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=xesYAIr2__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=i0lMAMb2__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=YuIEAPL2__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=tyMFAB33__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=1LMGADj3__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=26kUAFL3__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=7PNKAWT3__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=Md_DAZ33__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=M37OALv3__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=MfYPAOj3__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=r9K5AAf4__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=iVCUACf4__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=af4LADP4__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=HX4SAEv4__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=s_cfAG34__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=1V4UAJT4__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=qy4OAKv4__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=d_p_ANT4__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=fF7NAOr4__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=_VAIABT5__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=-NgZADf5__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=l2wGAFH5__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=ZBM5AH_5__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=s0-6AJ35__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=jPASALr5__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=s6YKANb5__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=7ltyAOn5__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=xJ9aAA76__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=GQAKADb6__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=fpOSAE76__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=tK06AWL6__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=l3OaAIP6__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=Lj1iAJD6__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=XKgLAK76__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=w72xAMr6__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=z3nvANb6__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=n_MaAeH6__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=l60FAPr6__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=nFUFAAv7__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=h9gJABj7__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=rFmmADT7__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=ipwxAEL7__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=6pLXAEz7__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=BYcDAGX7__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=zImkAXb7__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=BcCNAIP7__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=DCMMAI77__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=WwI_AJz7__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=lh2JAKX7__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=zyyQALf7__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=xsMSAMv7__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=GfYfAN37__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=5pNcAOr7__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=MieIAAL8__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=w0xeAA78__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=pYYDABf8__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=BwkOACn8__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=vlivADD8__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=PnoGADn8__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=nKwGAEr8__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=lm8RAFX8__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=YgAPAF78__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=exAQAG78__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=nKoFAH78__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=VZsQAJH8__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=o4HHAKH8__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=MJnYALD8__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=Id1BAML8__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=BcQKAMn8__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=R4xLAdP8__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=LBBZAdv8__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=4ZOAAOr8__8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=d8heAPT8__8J&astart=1350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=fRnoAP38__8J&astart=1360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=5uxBAA39__8J&astart=1370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=gVuzAB39__8J&astart=1380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=zq0NACT9__8J&astart=1390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=yKRAADH9__8J&astart=1400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=xZcIAD_9__8J&astart=1410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=aVUVAEj9__8J&astart=1420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=vtiCAFP9__8J&astart=1430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=RD-HAFz9__8J&astart=1440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=gk-pAGL9__8J&astart=1450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=JuCYAGv9__8J&astart=1460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=3LjOAXD9__8J&astart=1470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=F57WAHf9__8J&astart=1480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=4F1sAH_9__8J&astart=1490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=FiYMAIf9__8J&astart=1500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=0bggAI79__8J&astart=1510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=5igfAJj9__8J&astart=1520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=KH_6AJ79__8J&astart=1530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=xPvmAKT9__8J&astart=1540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=k44bAKv9__8J&astart=1550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=S0OzALb9__8J&astart=1560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=lWq0Ab39__8J&astart=1570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=HWiKAMT9__8J&astart=1580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=fgWBAMf9__8J&astart=1590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=PxIZAM_9__8J&astart=1600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=kCGzANn9__8J&astart=1610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=izM3AeD9__8J&astart=1620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=nHiJAOf9__8J&astart=1630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=gi4TAOv9__8J&astart=1640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=pAjBAPD9__8J&astart=1650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=2zqBAPf9__8J&astart=1660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=GHoJAPr9__8J&astart=1670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=Gc2DAP_9__8J&astart=1680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=6300175949274449304&after_author=5jHHAAf-__8J&astart=1690',

    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Campinas done...\n")
    all_faculty = [list(item) for item in set(tuple(sublist) for sublist in all_faculty)]
    return all_faculty

if __name__ == "__main__":
    unicamp()