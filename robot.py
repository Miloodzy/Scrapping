#!/usr/bin/env python
import mechanize
from bs4 import BeautifulSoup

print("hello")
br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_refresh(False)

html = br.open("https://www.kubii.fr/fr/40-raspberry-pi-3-2-et-b").read()
 
soup = BeautifulSoup(html, "html.parser")
name = soup.find_all('h5',{"itemprop":"name"})
price = soup.find_all('span',{"itemprop":"price"})
nameResponse=""
priceResponse=""

for a in name:
	nameResponse+=a.getText()

for b in price:	
	priceResponse+=b.getText()

print("Name : "+nameResponse)



    

