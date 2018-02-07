#!/usr/bin/env python
import mechanize
import sys
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
db = client.product

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
#br.set_proxies({"http": "proxypac.priv.gfi.fr/proxy.pac"}) 
br.set_handle_redirect(True)
br.set_handle_referer(True)

html = br.open("https://www.kubii.fr/").read()

br.select_form(nr=0)
br.form['search_query'] = sys.argv[1]
response = br.submit()

soup = BeautifulSoup(response, "html.parser")
name = soup.find_all('h5',{"itemprop":"name"})
price = soup.find_all('span',{"itemprop":"price"})
nameResponse=""
priceResponse=""

for a in name:
       	nameResponse+=a.getText()+'\n'
       	#print(a.getText())
for b in price:
       	priceResponse+=b.getText()+'\n'

spl=nameResponse.split('\n')
spq=priceResponse.split('\n')

for i in range (len(spl)):
	result = db.items.insert_one(
		{
			"name":spl[i],
			"price":spq[i]
		}
	)
print(result.inserted_id)

#print(spq[1])
#print(nameResponse)
