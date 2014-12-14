
#! Python3
from HTMLParser import HTMLParser
from pymongo import MongoClient
import os
import sys
from bs4 import BeautifulSoup
import requests
import ast
import json

#client = MongoClient()
#db = client.testingdata
#collection = db.files
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'}
def getitem1(html):
	x = 0
	string = html
	startingcrawl = requests.get("http://www.bol.com/nl/p/konig-cmp-satapci11-sata-pci-controllerkaart/1003004007645920/", headers=headers)
	startsoup = BeautifulSoup(startingcrawl.content, 'html.parser')
	cntent = startsoup.findAll("td", {"class": "specs_title"})
	titles = startsoup.find('h1',{"class": "bol_header clear_autoheight bottom_0"})
	titles = str(titles)
	titles = titles.replace("\n","") 	#
	titles = titles.replace("[","")		#
	titles = titles.replace("]","")		#
	titles = titles.replace("<h1 class=\"bol_header clear_autoheight bottom_0\" itemprop=\"name\">","")
	titles = titles.replace("</h1>","")	#
	titles = titles.replace(" ","_")	#
	titles = titles.replace("/","")
	text_file_doc = "{\"file_name\": \""+ titles+ "\", specs: ["
	while x <= len(cntent)-1:
		test = str(cntent[x])
		test = strip_tags(test).replace("\n", "")
		content = startsoup.findAll("td", {"class": "specs_descr"})
		test2 = str(content[x])
		text_file_doc+= "{\"" + strip_tags(test).replace("\n", "") +"\":\""
		invoer =  strip_tags(test2).replace("\n", "")
		invoer = invoer.strip()
		text_file_doc+= invoer +"\"}"
		if x != len(cntent)-1:
			text_file_doc += ","
		x+=1
	text_file_doc += "]}"
	client = MongoClient('145.24.222.229', 27017)
	db = client.Products
	collection = db.files
	print json.loads('{"1":"2"}')
	testfile = {'file' : titles, 'specs': [{ test : invoer}]}
	print text_file_doc
	collection.insert(text_file_doc)

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



if len(sys.argv) == 1:
	pad = "/Users/Brian/Documents/data/behuizingen"
else:
	pad = sys.argv[1]
x = 0

for file in os.listdir(pad):
	if file != ".DS_Store":
		if x < 1:
			f = open(os.path.join(pad, file))
			text = f.read()
			getitem1(text)
			#print text 
			#print "-------------" 
			x = 1
		#text_file_doc = {"file_name" : file, "contents" : text }
		#collection.insert(text_file_doc)

