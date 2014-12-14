#! Python3
#updated crawler
#imports.

from HTMLParser import HTMLParser
from pymongo import MongoClient
import os
import sys
import urlparse
import urllib
from bs4 import BeautifulSoup
import requests
import os.path
import time
from random import randrange
import re
import math
import time
import datetime




####-----Initialize Settings-----####
client = MongoClient()   # Connect to database
db = client.testingdata  #create database called TestingData
collection = db.files2  #Create collection named files 2( db.files2.find())

o=open("url.txt",'w')
url = "http://www.bol.com/nl/l/computer/computercomponenten-behuizingen/N/8474/index.html"
shorturl = "http://www.bol.com/nl/"
urls = [url]
stupidurls = []
doubleurl = []
visited = [url]
keepout = ["/inwinkelwagentje.html?productId=", "verlanglijstje/verlanglijstje.html?", "prijsoverzicht/?", "/b/computer/", "index.html" ]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'}
i = 0
x = 0
pagenum = [0]   #Because python uses Pointers u cannot change a Int in a variable, you need to wrap it into an object.
adjustedurl = [""] # wrap wrap into an object.
totalnumberofitems = [""]
def geturls(funcurl):
	startcrawl = requests.get(funcurl,headers=headers)
	startsoup = BeautifulSoup(startcrawl.content, 'html.parser')
	startitems = startsoup.find("div", {"id": "js_multiselect_results"})
	for tag in startitems.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if shorturl in tag['href'] and tag['href'] not in visited:
				if any(x in tag['href'] for x in keepout):
					stupidurls.append(tag['href'])
				elif tag['href'] in urls:
					doubleurl.append(tag['href'])
				else:
					o.write(tag['href'])
					o.write("\n")
					urls.append(tag['href'])

def gettotalitems(itemurl):
	totalitemstart = requests.get(itemurl,headers=headers)
	totalsoup = BeautifulSoup(totalitemstart.content, 'html.parser')
	totalitems = totalsoup("span",{"id": "sab_header_results_size"})
	totalnumberofit = str(totalitems)
	totalnumberofit = totalnumberofit.replace("<span class=\"tst_searchresults_nrFoundItems\" id=\"sab_header_results_size\">","")
	totalnumberofit = totalnumberofit.replace("</span>","")
	totalnumberofitems[0] = totalnumberofit
	return totalnumberofitems

def getnumber(length, newurl):
	i = 0
	if(length >= 48*i):
		pagenum[0] += 1
		i += 1
	urlparts = newurl
	urlparts = urlparts.split("index.html")
	adjustedurl[0] =  urlparts[0] + "page/" + str(pagenum[0]) + "/index.html"
	return pagenum, newurl;

def getitems(html):
	x = 0
	string = html

	startingcrawl = requests.get(html, headers=headers)

	startsoup = BeautifulSoup(startingcrawl.content, 'html.parser')
	cntent = startsoup.findAll("td", {"class": "specs_title"})
	price = startsoup.findAll("span",{"class" : "product-price-bol price-big"})
	if len(price) > 0:
		price = strip_tags(str(price[0]).replace("\n", ""))
	else:
		price = "Niet leverbaar"
	titles = startsoup.find('h1',{"class": "bol_header clear_autoheight bottom_0"})
	titles = strip_tags(str(titles).replace("\n",""))
	save = {}

	## EDIT ##
	save['Title'] = titles 
	##      ##
	save['specs'] = []
	while x <= len(cntent)-1:
		test = str(cntent[x])
		content = startsoup.findAll("td", {"class": "specs_descr"})
		test2 = str(content[x])
		invoer =  strip_tags(test2).replace("\n", "")
		invoer = invoer.strip()
		spectitle = strip_tags(test).replace("\n", "")
		if 'Verpakking' in spectitle:
			spectitle = "Verpakking"
		if "Besturingssysteem" in spectitle:
			spectitle = "Besturingssysteem"
		if "\"" in invoer:
			invoer = invoer.replace("\"", "-Inch ")
		if "." in spectitle:
			spectitle = spectitle.replace(".", "")
		if "Harde schrijf snelheid" in spectitle:
			spectitle = "Harde schijf snelheid (RPM)"
		if "Opslagcapaciteit" in spectitle:
			spectitle = "Opslagcapaciteit in GB (gigabyte) of TB (terabyte)"
		save['specs'].append({})
		save['specs'][x][spectitle] = invoer
		save['price'] = price
		x+=1
	with open("mongoinput.txt", 'a') as myFile:
		myFile.write(str(save) + "\n")
	collection.insert(save)

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


geturls(url)   #haal de eerste URL OP
gettotalitems(url) # Haal het totaal aantal items op (aangegeven op de pagina's)
urls.pop(0) #delete de eerste URL
getnumber(len(urls), url)
totalnumberofitems = str(totalnumberofitems).replace("[","").replace("]","").replace("'","").replace(".","")
while (48*x <= int(totalnumberofitems)):
	getnumber(len(urls),url)
	geturls(adjustedurl[0])
	x+=1

print len(urls)
o.close()
q=open("badurl.txt", 'w')
q.write(str(stupidurls))
q.close()
d=open("double.txt",'w')
d.write(str(doubleurl))
d.close()
print "we just got " + str(len(urls)) + " links to products!"
time.sleep(2)

with open('url.txt') as f:
	content = f.readlines()

linenumber = 0
for line in content:
	getitems(line)
	linenumber += 1
	client.close()
	print "line" + str(linenumber) + " crawled at ------------" + str(datetime.datetime.now().time())
	time.sleep(2)
