from bs4 import BeautifulSoup
import requests
import concurrent.futures

university = "Stanford"
country = "USA"

faculty_data = []

def get_faculty_data(href):
    indiv_url = "https://www.cs.stanford.edu" + href
    response = requests.get(indiv_url)
    new_html_content = response.text
    new_soup = BeautifulSoup(new_html_content, 'html.parser')

    extract_email = new_soup.find_all('a', href=lambda href: href and href.startswith('mailto:'))
    email = extract_email[0].get_text().strip() if extract_email else 'Email Not Provided'

    text_content = new_soup.find('h1').get_text().strip()

    print([university, country, text_content, email, indiv_url])
    faculty_data.append([university, country, text_content, email, indiv_url])

def stanford():
    url_os = "https://www.cs.stanford.edu/people-cs/faculty-research/operatingdistributed-systems"
    url_emb = "https://www.cs.stanford.edu/people-cs/faculty-research/robotics"

    response_os = requests.get(url_os)
    response_emb = requests.get(url_emb)
    html_content = response_os.text + response_emb.text

    soup = BeautifulSoup(html_content, 'html.parser')

    extract_webpage = soup.find_all('a', class_=None, id=None, href=lambda href: href and href.startswith('/people/'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_faculty_data, element.get('href')) for element in extract_webpage]
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if result:
                    faculty_data.append(result)
            except Exception as e:
                print(f"Error occurred: {e}")
    print()
    print("Stanford Done....")
    print()
    return faculty_data

if __name__ == "__main__":
    stanford()
