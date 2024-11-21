from urllib.parse import unquote

def get_next_url(soup):
    url_string = soup.find('button', class_="gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx")['onclick']
    url_string = "https://scholar.google.com" + url_string.replace("window.location='", "")[:-1]
    url_string = url_string.replace("\\x3d", "=").replace("\\x26", "&")
    return (unquote(url_string))

# from bs4 import BeautifulSoup
# import requests

# url = "https://scholar.google.com/citations?view_op=view_org&hl=en&org=4770128543809686866&before_author=pZf9_wemBQAJ&astart=0"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
# }

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, 'html.parser')

# print(get_next_url(soup))
