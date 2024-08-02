from bs4 import BeautifulSoup
import requests
import re
import redo.google_scholar

u_name = "City University Hong Kong"
country = "Hong Kong"

def city_uni_hk():

    url_1 = "https://www.cs.cityu.edu.hk/people/academic-staff"
    url_2 = "https://www.cs.cityu.edu.hk/people/teaching-staff"
    url_3 = "https://www.cs.cityu.edu.hk/people/affiliate-faculty"

    response_1 = requests.get(url_1)
    response_2 = requests.get(url_2)
    response_3 = requests.get(url_3)
    html_content = response_1.text + response_2.text + response_3.text

    soup = BeautifulSoup(html_content, 'html.parser')

    faculty_data = []

    keyword_list = ["operating system", "robotics", "kerrnel", "embedded system", "hardware", "computer architecture", "distributed system", "computer organization", "vlsi", "computer and system", "human-computer interaction", "human computer"]

    professors = soup.find_all('article', class_='person-card')

    for professor in professors:

        name = professor.find('div', class_="name").get_text().strip() if professor.find('div', class_="name") else "Name not found"

        name = name.split(" ")[1:-1]

        name = " ".join(name)

        profile = professor.find('div', class_="profile")

        links = profile.find_all('a')

        email = links[0]['href'][7:] if links[0] else "Email not found"
        link = links[1]['href'] if links[1] else "Link not found"

        research = professor.find('div', class_="interest").text[22:].strip() if professor.find('div', class_="interest") else "Research not found"

        found_keyword = any(re.search(re.escape(keyword), research.lower(), re.IGNORECASE) for keyword in keyword_list)

        if found_keyword:

            new_r = requests.get(link)
            new_soup = BeautifulSoup(new_r.text, 'html.parser')

            personal_webpage = None
            other_links_section = new_soup.find('h2', class_='subheader', string="Other Links")
            if other_links_section:
                links = other_links_section.find_next('li').find('a')['href']
                personal_webpage = links if links else None

            # Fallback to Google Scholar if personal webpage not found
            if not personal_webpage:
                personal_webpage = google_scholar.get_scholar_profile(name)

            faculty_data.append([u_name, country, name, email, link, personal_webpage])
            print([u_name, country, name, email, link, personal_webpage])

    print()
    print("City University Hong Kong done....")
    print()
    return faculty_data


# city_uni_hk()