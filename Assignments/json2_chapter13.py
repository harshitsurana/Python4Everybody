import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read().decode()
info=json.loads(html)
lst=list()
for counts in info['comments']:
    lst.append(int(counts['count']))
print(sum(lst))
