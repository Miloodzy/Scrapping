#!/usr/bin/env python
import mechanize
import sys
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://localhost:27017")
db = client.test

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_refresh(True)
br.addheaders = [('User-agent', 'Firefox')]

html = br.open("http://www.leboncoin.fr/annonces/offres/rhone_alpes").read()

br.select_form("f")
br.form['q'] = sys.argv[1] 
response = br.submit()
#print(response.read())
soup = BeautifulSoup(response, "html.parser")
name = soup.find_all('h2',{"itemprop":"name"})
#price = soup.find_all('h3',{"itemprop":"price"})


print(name)
#nameResponse=""
#priceResponse=""

#for i in range(len(name)):
#	print("mongoName = "+name[i].getText().replace(" ",""))
#	print("mongoPrice = "+price[i].getText().replace(" ",""))
#	result = db.item.insert_one(
#        	{
#                "name": mongoName,
#                "price": mongoPrice
#        	}
#	)

#print(result.inserted_id)


