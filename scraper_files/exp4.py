from bs4 import BeautifulSoup

# Sample HTML content
html_content = '''
<div class="col-md-6">
<h1>Professor Chan, Hubert T.H.</h1>
<strong>PhD <em>Carnegie Mellon</em><br /> BEng(CompSc) Programme Director; Associate Professor</strong><br /> <br /> Tel: (+852) 2857 8461<br /> Fax: (+852) 2559 8447<br /> Email: hubert@cs.hku.hk<br /> Homepage: <a href="https://www.cs.hku.hk/~hubert">https://www.cs.hku.hk/~hubert</a></div>
'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Locate the <div> tag with the class 'col-md-6'
div_tag = soup.find('div', class_='col-md-6')

# Extract and print all the text within the <div>
div_text = div_tag.get_text(separator="\n").strip()
print(div_text)
