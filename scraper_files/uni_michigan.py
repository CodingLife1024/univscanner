import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.GLOBAL_VARIABLES import *
from components.gscholar_indiv_page import search_faculty_list

u_name = "University of Michigan"
country = "United States"

all_faculty_uni_michigan = []

def get_faculty_data(link, headers):
    global all_faculty_uni_michigan
    all_faculty_uni_michigan += search_faculty_list(link, headers, u_name, country)[0]

def uni_michigan():
    global all_faculty_uni_michigan
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=4770128543809686866",
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=GnUzACDb_f8J&astart=10',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Go40AXt4_v8J&astart=20',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=RZoFAN-1_v8J&astart=30',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=pw17AFTo_v8J&astart=40',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=s0hqAEoA__8J&astart=50',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=RnEYAa8T__8J&astart=60',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=NnUAALcp__8J&astart=70',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=a4hHAdM9__8J&astart=80',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=s1gFAAJF__8J&astart=90',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=hfoBAFRN__8J&astart=100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=qKo_ARRU__8J&astart=110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=McA7AJlY__8J&astart=120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=DHEFAGhe__8J&astart=130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=IpqwAIll__8J&astart=140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=H6EUACdq__8J&astart=150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=OJUDAElv__8J&astart=160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=UIcaAPl1__8J&astart=170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=4g58APp6__8J&astart=180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=rnQAAHB-__8J&astart=190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=bMoKAU-C__8J&astart=200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=FHtZAO6E__8J&astart=210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=yNLhABiL__8J&astart=220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=C8IMAGON__8J&astart=230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=5c8jAaWT__8J&astart=240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=MzKJAXuV__8J&astart=250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=63oLAIuX__8J&astart=260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=i6EPAVWZ__8J&astart=270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=zbhEAH-d__8J&astart=280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=3pttANqg__8J&astart=290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Ky9JAGKi__8J&astart=300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=CqQlAH2k__8J&astart=310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=2GYAAOyl__8J&astart=320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=rjQDAMmn__8J&astart=330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=xAcvAdKp__8J&astart=340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=djqRAHis__8J&astart=350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=z48QAJyu__8J&astart=360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=7tKOAKSv__8J&astart=370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=NBcLAfGw__8J&astart=380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=9PBvAL2y__8J&astart=390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=NrOIAKSz__8J&astart=400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Ics8AUC2__8J&astart=410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=78IpAKe3__8J&astart=420',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=NERbAL64__8J&astart=430',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=HTt5AL66__8J&astart=440',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=eZ4mAeC7__8J&astart=450',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=TbkGAAC9__8J&astart=460',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=FQYAABm-__8J&astart=470',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=yDEdAPi-__8J&astart=480',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=gNxyAALA__8J&astart=490',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=-hkcAYjA__8J&astart=500',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=OvgPAPTA__8J&astart=510',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=uEYDAN3B__8J&astart=520',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=DEEqAKrC__8J&astart=530',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=ot9JAZrD__8J&astart=540',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=99kQAOTE__8J&astart=550',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Pp4JALbF__8J&astart=560',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=uf4EAKfG__8J&astart=570',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=HZwBABvI__8J&astart=580',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=35sBAPLI__8J&astart=590',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=ZGXWAF_J__8J&astart=600',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=OgRuANvJ__8J&astart=610',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=XUg7ADrK__8J&astart=620',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=3SEgABzL__8J&astart=630',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=hparAMPL__8J&astart=640',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=1jZCAOLM__8J&astart=650',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=qBuZAdzN__8J&astart=660',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=QSZTAI_O__8J&astart=670',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=J7MPABXP__8J&astart=680',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=i28BANbP__8J&astart=690',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=cw8LAIrQ__8J&astart=700',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=lOQEAEjR__8J&astart=710',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=JiPOADXS__8J&astart=720',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=RDn3ADTT__8J&astart=730',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=G0IgAADU__8J&astart=740',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=wWk8AFDU__8J&astart=750',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=54gCAOPU__8J&astart=760',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=KjFDAU_V__8J&astart=770',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=7ytoAKLV__8J&astart=780',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=XGqJAE_W__8J&astart=790',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=qzdVAKfW__8J&astart=800',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=SYcKAGTX__8J&astart=810',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=v0k6AQ7Y__8J&astart=820',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=bfISAKfY__8J&astart=830',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=42o0ACzZ__8J&astart=840',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=C6SHAKDZ__8J&astart=850',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=JsMNAEfa__8J&astart=860',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=1TWKANPa__8J&astart=870',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=jQECAFnb__8J&astart=880',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=t0_HAfzb__8J&astart=890',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=V_YVAX_c__8J&astart=900',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=3_E4ABPd__8J&astart=910',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=F9IKAJvd__8J&astart=920',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=h_8NACDe__8J&astart=930',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=3vk1AJLe__8J&astart=940',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Lc5_AOve__8J&astart=950',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=4jwmAEDf__8J&astart=960',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=rF4EAILf__8J&astart=970',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=4luGAOrf__8J&astart=980',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=gPIOATrg__8J&astart=990',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=av0CAIDg__8J&astart=1000',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=_keAANXg__8J&astart=1010',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=hOEvAGDh__8J&astart=1020',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=gPdTALXh__8J&astart=1030',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=OCsUAPTh__8J&astart=1040',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=wEUYAF_i__8J&astart=1050',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=pWsAAK7i__8J&astart=1060',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=hkOxAOHi__8J&astart=1070',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=U9MUAGbj__8J&astart=1080',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=66YWALHj__8J&astart=1090',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=7l_oAATk__8J&astart=1100',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=L4RtADjk__8J&astart=1110',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=nFufAaHk__8J&astart=1120',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=JOaCAcrk__8J&astart=1130',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=CkkxAALl__8J&astart=1140',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=pyQRAGLl__8J&astart=1150',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=_HIhALvl__8J&astart=1160',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=2RiyAC7m__8J&astart=1170',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=s4HWAI_m__8J&astart=1180',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=f9RrAPvm__8J&astart=1190',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=tHavAFHn__8J&astart=1200',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=wawJAIrn__8J&astart=1210',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=_DgfAMvn__8J&astart=1220',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=XxkSAPTn__8J&astart=1230',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=HN5DACTo__8J&astart=1240',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=kQSEAGvo__8J&astart=1250',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=5xP3AJPo__8J&astart=1260',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=uQIAAMDo__8J&astart=1270',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=ii8DAPjo__8J&astart=1280',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=c0kXAUvp__8J&astart=1290',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=daVbAJ7p__8J&astart=1300',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=BY0vAMrp__8J&astart=1310',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=BmwAACnq__8J&astart=1320',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=gIrZAGnq__8J&astart=1330',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=J9YBAJPq__8J&astart=1340',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=GPgRAO3q__8J&astart=1350',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=4DkYACfr__8J&astart=1360',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=TosiAGDr__8J&astart=1370',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Q_-0AIHr__8J&astart=1380',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=PkcCAOPr__8J&astart=1390',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=qgBRABPs__8J&astart=1400',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=vW4SAD_s__8J&astart=1410',
        'https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Rw23AGDs__8J&astart=1420',
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Michigan done...\n")
    all_faculty_uni_michigan = [list(item) for item in set(tuple(sublist) for sublist in all_faculty_uni_michigan)]
    return all_faculty_uni_michigan

if __name__ == "__main__":
    uni_michigan()