import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
from components.google_scholar import get_scholar_profile
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.google_scholar import get_scholar_profile
from components.GLOBAL_VARIABLES import keyword_list

u_name = "Brown University"
country = "United States"

faculty_data = []

def extract_profile_link(full_profile):
    profile_link_tag = full_profile.find("a", string="Profile")
    return "https://cs.brown.edu" + profile_link_tag.get("href") if profile_link_tag else "Not Found"

def extract_home_page(full_profile, name):
    home_page_tag = full_profile.find("a", string="Home Page")
    return home_page_tag.get("href") if home_page_tag else get_scholar_profile(name)

def extract_research_areas(full_profile):
    research_areas_tag = full_profile.find("li", class_="profile-areas")
    return research_areas_tag.get_text().strip() if research_areas_tag else "Not Found"

def get_faculty_data(name_tag, headers):
    name = name_tag.get_text().strip()

    full_profile = name_tag.find_parent("li")

    if full_profile:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_profile_link = executor.submit(extract_profile_link, full_profile)
            future_home_page = executor.submit(extract_home_page, full_profile, name)
            future_research_areas = executor.submit(extract_research_areas, full_profile)

            profile_link = future_profile_link.result()
            home_page = future_home_page.result()
            research_areas = future_research_areas.result()

            found_keyword = any(re.search(re.escape(keyword), research_areas.lower()) for keyword in keyword_list)

            email = profile_link.split("/")[-2] + "@cs.brown.edu" if profile_link != "Not Found" else "Not Found"

            if found_keyword:
                new_r = requests.get(profile_link, headers=headers, verify=False)

                print([u_name, country, name, email, profile_link, home_page])
                faculty_data.append([u_name, country, name, email, profile_link, home_page])

def brown_uni():
    url = "http://cs.brown.edu/people/faculty/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
    }
    r = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(r.text, "html.parser")

    names = soup.find_all("li", class_="profile-name")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, name, headers) for name in names]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Ensure exceptions are raised
            except Exception as e:
                print(f"Error occurred: {e}")

    print("\nBrown University done...\n")
    return faculty_data


if __name__ == "__main__":
    brown_uni()