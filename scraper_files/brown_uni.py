import requests
import re
from bs4 import BeautifulSoup
from components.google_scholar import get_scholar_profile

u_name = "Brown University"
country = "USA"

def brown_uni():
    url = "http://cs.brown.edu/people/faculty/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
    }
    r = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = ["operating system", "robotics", "kernel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction"]

    faculty_data = []

    names = soup.find_all("li", class_="profile-name")

    for name_tag in names:
        name = name_tag.get_text().strip()

        # Adjusting to find the correct full profile
        full_profile = name_tag.find_parent("li")

        if full_profile:
            profile_link_tag = full_profile.find("a", string="Profile")
            profile_link = "https://cs.brown.edu" + profile_link_tag.get("href") if profile_link_tag else "Not Found"

            home_page_tag = full_profile.find("a", string="Home Page")
            home_page = home_page_tag.get("href") if home_page_tag else get_scholar_profile(name)

            research_areas_tag = full_profile.find("li", class_="profile-areas")
            research_areas = research_areas_tag.get_text().strip() if research_areas_tag else "Not Found"

            found_keyword = any(re.search(re.escape(keyword), research_areas.lower()) for keyword in keyword_list)

            email = profile_link.split("/")[-2] + "@cs.brown.edu" if profile_link != "Not Found" else "Not Found"

            if found_keyword:
                new_r = requests.get(profile_link, headers=headers, verify=False)

                print([u_name, country, name, email, profile_link, home_page])
                faculty_data.append([u_name, country, name, email, profile_link, home_page])

    print()
    print("Brown University Done....")
    print()
    return faculty_data

brown_uni()