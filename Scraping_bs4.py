from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

#Ignore SSl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html  = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

#Retrieve all of the span tags
tags = soup('span')
total = 0
for tag in tags:
   y = str(tag)
   x = (re.findall('[0-9]+',y))
   for element in x:
        #if element.isdigit():
      # adding the element to the total
            total += int(element)
print(total)
