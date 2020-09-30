# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
counts=int(input('Count-'))
position=int(input('Position-'))
for count in range(counts-1):
    tag=tags[position-1]
    html = urllib.request.urlopen(tag.get('href', None), context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
print(tags[position-1].contents[0])
