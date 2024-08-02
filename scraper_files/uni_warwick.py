import requests
from bs4 import BeautifulSoup
import re
import redo.google_scholar

u_name = "University of Warwick"
country = "UK"

def uni_warwick():
    url = "https://warwick.ac.uk/fac/sci/dcs/people/summaries/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    try:
        r = requests.get(url, headers=headers, verify=True)  # Set verify=True for certificate verification
        r.raise_for_status()  # Raise an exception for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        # Handle the error gracefully, possibly logging it or retrying
        raise SystemExit(e)

    # Getting the soup by parsing the HTML response
    soup = BeautifulSoup(r.text, "html.parser")

    keyword_list = [
        "operating system", "robotics", "kernel", "embedded system", "hardware",
        "computer architecture", "distributed system", "computer organization",
        "vlsi", "computer and system", "human-computer interaction", "human computer"
    ]

    faculty_data = []

    # Find all article elements with the class "card"
    faculty_divs = soup.find_all('div', class_='entryContent')

    # Loop through each faculty div
    for faculty in faculty_divs:
        # Extract name
        name = faculty.find('h2').text.strip()

        title = faculty.find('p').text.strip() if faculty.find('p') else "Not Found"

        if "lecturer" in title.lower() or "professor" in title.lower():
            link_tag = faculty.find('a')
            if link_tag:
                link = "https://warwick.ac.uk/" + link_tag['href'] if link_tag['href'].startswith("/fac") else link_tag['href']
                # print(name, link)

                try:
                    new_r = requests.get(link, headers=headers, verify=True)
                    new_r.raise_for_status()
                except requests.exceptions.RequestException as e:
                    print(f"Request failed for {link}: {e}")
                    continue

                new_soup = BeautifulSoup(new_r.text, "html.parser")

                content = new_r.text

                found_keyword = any(re.search(re.escape(keyword), content, re.IGNORECASE) for keyword in keyword_list)

                if found_keyword:
                    email_links = new_soup.find('a', href=lambda href: href and href.startswith("mailto:"))
                    if email_links:
                        email = email_links['href'][7:]
                    else:
                        email = "Email not found"

                    strong_tag = new_soup.find('strong', string='Website')

                    if strong_tag:
                        next_a_tag = strong_tag.find_next('a')
                        if next_a_tag:
                            website_link = next_a_tag['href']
                        else:
                            website_link = google_scholar.get_scholar_profile(name)
                    else:
                        website_link = google_scholar.get_scholar_profile(name)

                    print([u_name, country, name, email, link, website_link])
                    faculty_data.append([u_name, country, name, email, link, website_link])

    print()
    print("Warwick done....")
    print()

    return faculty_data
