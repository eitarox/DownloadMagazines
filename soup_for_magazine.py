import requests
import urllib3
from bs4 import BeautifulSoup

res = requests.get('https://www.google.com/')
soup = BeautifulSoup(res.text, 'html.parser')

title_text = soup.find('title').get_text
print(title_text)

#
# http = urllib3.PoolManager()
#
# http = urllib3.PoolManager(
#     cert_reqs='CERT_REQUIRED',
#     ca_certs=certifi.where())
