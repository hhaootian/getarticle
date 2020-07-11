# -*- coding: utf-8 -*-

import requests
import re
import time

class GetPaper(object):
	'''
	Download scientific papers given DOI, website, 
	title, or research field
	'''

	def __init__(self):
		self.SCIHUB = 'https://sci-hub.tw/'
		self.SCHOLAR = "https://scholar.google.com/scholar?start=0&q="
		self.url_collection = []
		self.doi_collection = []
		self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; \
			Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, \
				like Gecko) Version/5.0.4 Safari/533.20.27'}


	def _get_url_doi(self, url):
		print(url)
		r = requests.get(url, headers = self.headers)
		web_content = r.content.decode('utf-8', errors='replace')

		start_index = web_content.index("location.href=\'") + 15
		end_index = web_content[start_index+1:].index("'") + start_index + 1
		
		cur_pdf_url = web_content[start_index:end_index]
		if "https:" not in cur_pdf_url:
			cur_pdf_url = "https:" + cur_pdf_url

		self.url_collection.append(cur_pdf_url)


	def _get_url_search(self, url):
		r = requests.get(url, headers = self.headers)
		web_content = r.content.decode('utf-8', errors='replace')
		loc_list = web_content.split("doi/abs")[1:]
		for item in loc_list:
			print(item[1:item.index("\"")])
			self.paper(item[1:item.index("\"")])

	def paper(self, doi):
		if doi not in self.doi_collection:
			self.doi_collection.append(doi)
			url = self.SCIHUB + doi
			self._get_url_doi(url)

	
	def search(self, search, num_of_page = 1):
		if not search:
			raise ValueError("Please input title/keyword/author !")

		search = "+".join(re.sub(r'[^\w\s]', ' ', search).split())
		url = self.SCHOLAR + search
		for i in range(0, num_of_page):
			print(url[:41] + str(i) + url[41:])
			self._get_url_search(url[:41] + str(i-1) + url[41:])


	def download(self, direction="."):
		if not self.url_collection:
			raise ValueError("Empty DOI !")

		print("Downloading %d papers" %len(self.url_collection))
		while self.url_collection:
			url = self.url_collection.pop()
			open("%s/%s.pdf" %(direction, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())),
			 'wb').write(requests.get(url, allow_redirects=True).content)

