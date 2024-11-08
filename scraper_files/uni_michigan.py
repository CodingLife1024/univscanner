import requests
from bs4 import BeautifulSoup
import sys
import os
import re
import concurrent.futures
import pprint

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import *
from components.gscholar_indiv_page import search_faculty_list

u_name = "University of Michigan"
country = "United States"

all_faculty = []

def get_faculty_data(link, headers):
    global all_faculty
    all_faculty += search_faculty_list(link, headers, u_name, country)[0]

def uni_michigan():
    global all_faculty
    links = [
        "https://scholar.google.com/citations?view_op=view_org&org=4770128543809686866",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=GnUzAD3b_f8J&astart=10",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Go40AZt4_v8J&astart=20",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=RZoFAPe1_v8J&astart=30",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=pw17AFzo_v8J&astart=40",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=s0hqAFQA__8J&astart=50",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=RnEYAa8T__8J&astart=60",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=NnUAAL0p__8J&astart=70",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=a4hHAew9__8J&astart=80",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=s1gFAARF__8J&astart=90",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=hfoBAGVN__8J&astart=100",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=qKo_ARtU__8J&astart=110",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=McA7AKNY__8J&astart=120",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=DHEFAGpe__8J&astart=130",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=IpqwAJZl__8J&astart=140",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=H6EUACdq__8J&astart=150",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=OJUDAExv__8J&astart=160",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=UIcaAP51__8J&astart=170",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=4g58AA97__8J&astart=180",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=nhaQAH9-__8J&astart=190",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=bMoKAVOC__8J&astart=200",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=FHtZAPaE__8J&astart=210",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=yNLhABWL__8J&astart=220",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=C8IMAGON__8J&astart=230",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=5c8jAbGT__8J&astart=240",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=e1ACAJKV__8J&astart=250",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=63oLAIuX__8J&astart=260",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=i6EPAVWZ__8J&astart=270",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=zbhEAH-d__8J&astart=280",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=3pttANqg__8J&astart=290",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=Ky9JAGGi__8J&astart=300",
        "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&after_author=CqQlAHuk__8J&astart=310"
    ]

    # for link in links:
    #     # print("Fetching URL..." + link + "\n")
    #     all_faculty += search_faculty_list(link, headers, u_name, country)[0]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nUniversity of Michigan done...\n")
    # print(len(all_faculty))
    return all_faculty

if __name__ == "__main__":
    uni_michigan()