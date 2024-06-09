import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_scholar_profile_link(professor_name, university_name):
    # URL encode the professor name and university name for the query
    query = professor_name.replace(" ", "+") + "+" + university_name.replace(" ", "+")
    url = f"https://scholar.google.com/citations?view_op=search_authors&mauthors={query}&hl=en&oi=ao"

    # Send a GET request to Google Scholar
    response = requests.get(url)

    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first profile link
    profile_link = None
    first_a_tag = soup.find('a', {'class': 'gs_ai_pho'})
    if first_a_tag:
        profile_link = urllib.parse.urljoin('https://scholar.google.com', first_a_tag['href'])

    return profile_link

# Example usage
professor_name = "mauricio alvarez"
university_name = "University of Manchester"
profile_link = get_scholar_profile_link(professor_name, university_name)
if profile_link:
    print(f"Google Scholar profile link: {profile_link}")
else:
    print("Profile not found.")
