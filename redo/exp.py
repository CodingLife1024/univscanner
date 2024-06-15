import requests
from bs4 import BeautifulSoup

def get_personal_homepage(faculty_url, headers):
    try:
        response = requests.get(faculty_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {faculty_url}: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Search for the personal homepage link
    personal_homepage_tag = soup.find('a', href=True, string='Personal Homepage')
    if personal_homepage_tag:
        return personal_homepage_tag['href']
    else:
        return "Personal Homepage not found"

def print_website_text(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    # Print all the text from the website
    print(soup.get_text())

# URL of the specific faculty page
faculty_url = "https://www2.eecs.berkeley.edu/Faculty/Homepages/abbeel.html"

# Headers to use in the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# Get and print the personal homepage
personal_homepage = get_personal_homepage(faculty_url, headers)
print(f"Personal Homepage: {personal_homepage}")

# Print all the text from the faculty webpage
print("Text of the faculty webpage:")
print_website_text(faculty_url, headers)

# Optionally, print all the text from the personal homepage if it exists
if personal_homepage != "Personal Homepage not found":
    print("Text of the personal homepage:")
    print_website_text(personal_homepage, headers)
