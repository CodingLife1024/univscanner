import requests
import warnings
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3
warnings.simplefilter('ignore', InsecureRequestWarning)

url = "https://www.cse.cuhk.edu.hk/research/computer-engineering/"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'}

r = requests.get(url, headers=headers, verify=False)

if r.status_code == 200:
    print("Request successful")
else:
    print(f"Request failed with status code {r.status_code}")

print(r.text)