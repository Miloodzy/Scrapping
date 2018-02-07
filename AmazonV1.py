#!/usr/bin/env python
import mechanize
import sys
from bs4 import BeautifulSoup

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_refresh(True)
br.addheaders = [('User-agent', 'Firefox')]

html = br.open("https://www.amazon.fr").read()

br.select_form(name="site-search")
br.form['field-keywords'] = sys.argv[1]
response = br.submit()

#print(response['title'])
#print(response)
soup = BeautifulSoup(response, "html.parser")
name = soup.find_all('h2',{"class":"a-size-medium s-inline s-access-title a-text-normal"})
price = soup.find_all('span',{"class":"a-offscreen"})
#nameResponse=""
#priceResponse=""

for a in name:
        print(a['data-attribute'])
        #print(a.getText())
for b in price:
        print(b.getText()+'\n')

#print("Name : "+'\n'+nameResponse)
#print("Name : "+'\n'+nameResponse+'\n\n'+"Price : "+'\n'+priceResponse)

