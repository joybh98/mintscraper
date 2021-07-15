import requests
import json
import re
from bs4 import BeautifulSoup
from requests.api import head

section=input("Enter Section: ")
base_url="http://livemint.com/"
URL=base_url+section
page=requests.get(URL)

soup=BeautifulSoup(page.content,'html.parser')

# there are total 3 <script type='application/ld+json> tags, only 3rd needed that's why [3]
articles=soup.find_all('script',type='application/ld+json')[3].string.strip()

site_json=json.loads(articles)

headlines=[]
description=[]
url=[]
for d in site_json['itemListElement']:
    headlines.append(d.get('name'))
    description.append(d.get('description'))
    url.append(d.get('url'))

def convert_tojson(arr):
    jsonconv=json.dumps(arr)
    return jsonconv

convert_tojson(headlines)
convert_tojson(description)
convert_tojson(url)

print(headlines)