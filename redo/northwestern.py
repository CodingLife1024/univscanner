import requests
from bs4 import BeautifulSoup

def northwestern():
    url = "https://www.mccormick.northwestern.edu/computer-science/people/faculty/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # Send a GET request to the URL
    r = requests.get(url, headers=headers)

    # Parse the page content
    soup = BeautifulSoup(r.text, "html.parser")

    # Find all div elements with the class "faculty-info"
    d = soup.find_all('div', class_='faculty-info')

    for i in d:
        name = i.find('h3').text
        link = i.find('a', class_=None)['href'] if i.find('a', class_=None) else "Link not Found"
        email = i.find('a', class_='mail_link')['href'][7:] if i.find('a', class_='mail_link') else "Email not Found"

        print(name, link, email)

# Call the function
northwestern()
