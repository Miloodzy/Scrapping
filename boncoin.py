#!/usr/bin/env python
import mechanize
import sys
from bs4 import BeautifulSoup

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_refresh(False)

html = br.open("https://www.leboncoin.fr/annonces/offres/rhone_alpes/").read()

br.select_form(nr=0)
br.form['q'] = sys.argv[1] 
response = br.submit()

soup = BeautifulSoup(html, "html.parser")
name = soup.find_all('h2',{"itemprop":"name"})
price = soup.find_all('h3',{"itemprop":"price"})
nameResponse=""
priceResponse=""

for a in name:
        print(a.getText())
for b in price:
        print(b.getText())

#print("Name : "+'\n'+nameResponse)
#print("Name : "+'\n'+nameResponse+'\n\n'+"Price : "+'\n'+priceResponse)

