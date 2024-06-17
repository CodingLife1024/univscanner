import requests
from bs4 import BeautifulSoup

# URL of the faculty search page
url = "https://samueli.ucla.edu/search-faculty/#cs"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the container that holds the faculty information
    faculty_list = soup.find_all('div', class_='faculty-member')

    for faculty in faculty_list:
        # Extract faculty details
        name = faculty.find('h3', class_='faculty-name').text.strip()
        title = faculty.find('p', class_='faculty-title').text.strip()
        department = faculty.find('p', class_='faculty-department').text.strip()
        email = faculty.find('a', class_='faculty-email').get('href').replace('mailto:', '')
        phone = faculty.find('p', class_='faculty-phone').text.strip() if faculty.find('p', class_='faculty-phone') else 'N/A'

        # Print or store the extracted information
        print(f"Name: {name}")
        print(f"Title: {title}")
        print(f"Department: {department}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print('-' * 20)
else:
    print("Failed to retrieve the webpage")

