#! Python3
from HTMLParser import HTMLParser
from pymongo import MongoClient
from bs4 import BeautifulSoup
from random import randrange
from itertools import islice
from email.mime.text import MIMEText
import os, sys, urlparse, urllib, requests, os.path, time, re, math, datetime, smtplib, csv, traceback

client = MongoClient()
database = client.Products
prijsClient = MongoClient()
prijsdata = prijsClient.Prijzen
prijsColl = prijsdata.Prijs

csvfile = "pricewatch.csv"
urlfile = open("url.txt",'w') #Used to traceback which url gives us the error.
x = sys.argv[1]
print sys.argv[2]
try:
	x = int(x)
except ValueError as error:
	print "Stopping script"
	print "----------------------"
	print "Reason  =  "
	sys.exit("Argument 1 should be of type INT")
starturls = ["http://www.bol.com/nl/l/computer/computercomponenten-koeling/N/16457/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-behuizingen/N/8474/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-controllers/N/16436/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-geheugen-toebehoren/N/16438/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-inbouw-dataopslag/N/16445/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-netwerk/N/16449/index.html",
"http://www.bol.com/nl/l/computer/dataopslag-geheugen-optical-drives/N/7115/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-moederborden-toebehoren/N/16478/index.html",
"http://www.bol.com/nl/l/computer/dataopslag-geheugen-netwerkopslag-nas/N/7116/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-geluidskaarten/N/8476/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-processoren/N/16482/index.html",
"http://www.bol.com/nl/l/computer/computercomponenten-energie/N/16488/index.html"]
Collections = ['Koeling','Behuizingen','Controllers','Geheugen','Hardeschijf','Netwerk','OptischeDrivers','Moederborden','NetwerkOpslag','Geluidskaarten','Processoren','Energie']
collection = database[Collections[x]]
url = starturls[x]
shorturl = "http://www.bol.com/nl/"
urls, falseurls, doubleurls, visited = [],[],[], [url]
keepout = ["/inwinkelwagentje.html?productId=", "verlanglijstje/verlanglijstje.html?", "prijsoverzicht/?", "/b/computer/", "index.html"]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'}
i, y = 0,0
pagenum = [0]
runtime = 0
adjustedurl, totalnumberofitems = [""], [""]
def geturls(functionurl, runtime):
	startCrawl = requests.get(functionurl, headers=headers)
	mainHtml = BeautifulSoup(startCrawl.content, 'html.parser')
	mainItems = mainHtml.find("div",{"id": "js_multiselect_results"})
	for tag in mainItems.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if shorturl in tag['href'] and tag['href'] not in visited:
			if any(x in tag['href'] for x in keepout):
				falseurls.append(tag['href'])
			elif tag['href'] in urls:
				doubleurls.append(tag['href'])
			else:
				urlfile.write(tag['href'] + "\n")
				urls.append(tag['href'])

	totalItemsStart = str(mainHtml.find("span",{"id": "sab_header_results_size"}))
	if runtime == 1:
		totalnumberofitems[0] = totalItemsStart
		totalnumberofitems[0] = strip_tags(totalnumberofitems[0])
	return totalnumberofitems

def getnumber(length, newurl):
	q = 0
	if(length >= 48*q):
		pagenum[0] +=1
		q+=1
	urlparts = newurl.split("index.html")
	adjustedurl[0] = urlparts[0] + "page/" + str(pagenum[0]) + "/index.html"

def getitems(html, var):
	e, size, sizeIndex = 0,0,0
	mongoInput = {}
	startingCrawl = requests.get(html, headers=headers)
	startHTML = BeautifulSoup(startingCrawl.content, 'html.parser')
	beschrijving = startHTML.findAll("p", {"itemprop" : "description"})
	for value in beschrijving:
		kenmerken = value.findAll("ul", {"class" : "default_listitem"})
		if len(kenmerken) > 0:
			li = kenmerken[0].findChildren()
			while sizeIndex < len(li):
				if "<br/>" in str(li[sizeIndex]):
					li.pop(sizeIndex)
				sizeIndex+=1
			mongoInput['breschijving'] = []
			while size < len(li):
				invoerelement = strip_tags(str(li[size]))
				mongoInput['beschrijving'].append({})
				invoerelement = invoerelement.split(":")
				mongoInput['beschrijving'][size]['name'] = invoerelement[0]
				if len(invoerelement) > 1:
					mongoInput['beschrijving'][size]['value'] = invoerelement[1]
				size+=1
	beschrijving = strip_tags(str(beschrijving)).replace("\"","")
	contentTitle = startHTML.findAll("td", {"class": "specs_title"})
	contentWaarde = startHTML.findAll("td",{"class": "specs_descr"})
	prijs = startHTML.findAll("span",{"class": "product-price-bol price-big"})
	if len(prijs) > 0:
		prijs = strip_tags(str(prijs[0]).replace("\n",""))
	else:
		prijs = "Niet leverbaar"
	titles = startHTML.find("h1",{"class": "bol_header clear_autoheight bottom_0"})
	titles = strip_tags(str(titles).replace("\n",""))
	mongoInput['titles'] = titles
	mongoInput['specs'] = []
	while e <= len(contentTitle)-1:
		naam = strip_tags(unicode(str(contentTitle[e]), "utf-8")).replace("\n","")
		waarde = strip_tags(unicode(str(contentWaarde[e]), "utf-8")).replace("\n", "").strip()
		if "Verpakking" in naam:
			naam = "Verpakking"
		elif "Besturingssysteem" in naam:
			naam = "Besturingssysteem"
		elif "." in naam:
			naam = naam.replace(".","\uff0E")
		elif "Harde schijf snelheid" in naam:
			naam = "Harde schijf snelheid (RPM)"
		elif "Opslagcapaciteit" in naam:
			naam = "Opslagcapaciteit in GB (gigabyte) of TB (terabyte)"
		if "\"" in waarde:
			waarde  = waarde.replace("\"", "-Inch")
		mongoInput['specs'].append({})
		mongoInput['specs'][e]['name'] = naam
		mongoInput['specs'][e]['value'] = waarde
		mongoInput['price'] = prijs
		mongoInput['description'] = beschrijving
		e+=1
	collection.insert(mongoInput)
	if sys.argv[2] == "false":
		print "false"
		writeprices(prijs, titles)
	else:
		updateprices(prijs, titles)

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

def writeprices(prijs, titles):
	today = str(datetime.date.today())
	print today
	prijsColl.insert({today:prijs, 'titles':titles})

def updateprices(prijs, titles):
	today = str(datetime.date.today())
	print "hello"
	prijsColl.update({'titles':titles}, {'$set':{today:prijs}})


try:
	print url
	geturls(url, 1)
	urls.pop(0)
	getnumber(len(urls), url)
	totalnumberofitems = str(totalnumberofitems).replace("[","").replace("]","").replace("'","").replace(".","")
	print totalnumberofitems
	while (48*x <= int(totalnumberofitems)):
		print len(urls)
		getnumber(len(urls),url)
		geturls(adjustedurl[0], 0)	
		time.sleep(5)
		x+=1
except Exception as e:
	error()


urlfile.close()
print("we just got " + str(len(urls)) + " links to products!")
time.sleep(2)


with open('url.txt') as f:
	content = f.readlines()

linenumber = 0
try:
	for line in content:
		getitems(line, linenumber)
		linenumber += 1
		client.close()
		print("line" + str(linenumber) + " crawled at ------------" + str(datetime.datetime.now().time()))
		time.sleep(1)
	updateprices("12345,3", "Nexus Nexus LXM-8200")
except Exception as e:
	error()