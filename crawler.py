#! Python3
#updated crawler
#imports.
#Code starts at line number 190
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
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
import csv
import traceback
from itertools import islice

####-----Initialize Settings-----####
client = MongoClient()   # Connect to database
db = client.Products  #create database called Products
collection = db.allProducts  #Create collection named allProducts( db.allProducts.find())
csvfile = "pricewatch.csv"  #create a string with the name of a new CSV FILE
o=open("url.txt",'w') 		#Open a file and name it url.txt with the WRITE option
'''
http://www.bol.com/nl/l/computer/computercomponenten-koeling/N/16457/index.html
http://www.bol.com/nl/l/computer/computercomponenten-behuizingen/N/8474/index.html
http://www.bol.com/nl/l/computer/computercomponenten-controllers/N/16436/index.html
http://www.bol.com/nl/l/computer/computercomponenten-geheugen-toebehoren/N/16438/index.html
http://www.bol.com/nl/l/computer/computercomponenten-inbouw-dataopslag/N/16445/index.html
http://www.bol.com/nl/l/computer/computercomponenten-netwerk/N/16449/index.html
http://www.bol.com/nl/l/computer/dataopslag-geheugen-optical-drives/N/7115/index.html
http://www.bol.com/nl/l/computer/computercomponenten-moederborden-toebehoren/N/16478/index.html
http://www.bol.com/nl/l/computer/dataopslag-geheugen-netwerkopslag-nas/N/7116/index.html
http://www.bol.com/nl/l/computer/computercomponenten-geluidskaarten/N/8476/index.html
http://www.bol.com/nl/l/computer/computercomponenten-processoren/N/16482/index.html
http://www.bol.com/nl/l/computer/computercomponenten-energie/N/16488/index.html
'''

url = "http://www.bol.com/nl/l/computer/computercomponenten-geheugen-toebehoren/N/16438/index.html"
itemtype = True
shorturl = "http://www.bol.com/nl/"
urls = []
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

def getitems(html,var, itemtype ):
	x = 0
	size= 0
	sizeindex = 0
	save = {}
	string = html
	startingcrawl = requests.get(html, headers=headers)
	startsoup = BeautifulSoup(startingcrawl.content, 'html.parser')
	if itemtype:
		beschrijving = startsoup.findAll("p",{"itemprop" : "description"})
		for value in beschrijving:
			kenmerken = value.findAll("ul", {"class" : "default_listitem"})
			if len(kenmerken) > 0:
				li = kenmerken[0].findChildren()
				while sizeindex < len(li):
					if "<br/>" in str(li[sizeindex]):
						li.pop(sizeindex)
					sizeindex+=1
				save['beschrijving'] = []
				while size < len(li):
					element = str(li[size])
					invoerelement = strip_tags(element).replace(".","")
					save['beschrijving'].append({})
					invoerelement = invoerelement.split(":")
					save['beschrijving'][size]['name'] = invoerelement[0]
					if len(invoerelement) > 1:
						save['beschrijving'][size]['value'] = invoerelement[1]
					size+=1
	beschrijving = strip_tags(str(beschrijving)).replace("\"","").replace(".","")
	cntent = startsoup.findAll("td", {"class": "specs_title"})
	price = startsoup.findAll("span",{"class" : "product-price-bol price-big"})
	if len(price) > 0:
		price = strip_tags(str(price[0]).replace("\n", ""))
	else:
		price = "Niet leverbaar"
	titles = startsoup.find('h1',{"class": "bol_header clear_autoheight bottom_0"})
	titles = strip_tags(str(titles).replace("\n",""))

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
		save['specs'][x]['name'] = spectitle
		save['specs'][x]['value'] = invoer
		save['price'] = price
		save['description'] = beschrijving
		x+=1
	with open("mongoinput.txt", 'a') as myFile:
		myFile.write(str(save) + "\n")
	collection.insert(save)
	writeprices(price, titles)
	updateprices(price, titles, var)

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

def error():
	msg = MIMEText("A error occured: %s. <br> Near line number: <span style='Color:red'>%s</span> <p> <b>Please note that this is not the exact line number!</b> <p><p> Full traceback: %s" % (e, sys.exc_traceback.tb_lineno, traceback.format_exc()), 'html')
	msg['Subject'] = 'Crawler raised an error!' 
	msg['From'] = 'brian_van_den_heuvel@me.com'
	reciepients = ['brian_van_den_heuvel@me.com', 'joost1235@hotmail.com']
	msg['To'] = ", ".join(reciepients)

	# Send the message via gmail's SMTP server.
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("brian.van.den.heuvel2@gmail.com", "nouria123az")
	s.sendmail(msg['From'], reciepients, msg.as_string())
	s.quit()

def writeprices(prijs, titel):
	price = prijs
	titels = titel
	with open(csvfile, 'a') as csvfiler:
		filewrite = csv.writer(csvfiler)
		filewrite.writerow([titels, price, 'END'])

def updateprices(prijstitel, titelprijs, var):
	with open(csvfile, 'r') as csvfileadjust:
		filereader = csv.reader(csvfileadjust)
		row = list(islice(filereader,var+1))[-1]
		if titelprijs in row:
			ind = row.index('END')
			lastprijs = row[ind-1]
			print lastprijs
			if lastprijs != prijstitel:
				row.pop(ind)
				row.append(prijstitel)
				row.append("END")
			with open('out.csv', 'a') as out:
				tester = csv.writer(out)
				tester.writerow(row)
		else: 
			with open('out.csv', 'a') as out:
				tester = csv.writer(out)
				tester.writerow(row)



try:
	geturls(url)   #haal de eerste URL OP
	gettotalitems(url) # Haal het totaal aantal items op (aangegeven op de pagina's)
	urls.pop(0) #delete de eerste URL
	getnumber(len(urls), url)
	totalnumberofitems = str(totalnumberofitems).replace("[","").replace("]","").replace("'","").replace(".","")
	print totalnumberofitems
	while (48*x <= int(totalnumberofitems)):
		print len(urls)
		getnumber(len(urls),url)
		geturls(adjustedurl[0])	
		print adjustedurl
		time.sleep(5)
		x+=1
except Exception as e:
	print e


o.close()
q=open("badurl.txt", 'w')
q.write(str(stupidurls))
q.close()
d=open("double.txt",'w')
d.write(str(doubleurl))
d.close()
print("we just got " + str(len(urls)) + " links to products!")
time.sleep(2)

try:
	with open('url.txt') as f:
		content = f.readlines()

	linenumber = 0
	for line in content:
		getitems(line, linenumber, itemtype)
		linenumber += 1
		client.close()
		print("line" + str(linenumber) + " crawled at ------------" + str(datetime.datetime.now().time()))
		time.sleep(1)
except Exception as e:
	error()



