# -*- coding: utf-8 -*-

import requests
import re
import time
import warnings
from os.path import expanduser

class GetArticle(object):
    '''
    Download scientific papers given DOI, website, 
    title, or research field
    '''
    def __init__(self):
        self.SCIHUB = 'https://sci-hub.se/'
        self.SCHOLAR = "https://scholar.google.com/scholar?start=0&q="
        self._url_collection = []
        self._doi_collection = []
        self._title_collection = []
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; \
            Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, \
                like Gecko) Version/5.0.4 Safari/533.20.27'}


    def _get_url_doi(self, url):
        '''
        get DOI and web address for download
        '''
        r = requests.get(url, headers = self.headers)
        web_content = r.content.decode('utf-8', errors='replace')
        assert ("location.href=\'" in web_content), "Paper not found!"

        doi = web_content.split(self.SCIHUB)[1].split("\"")[0]
        try:
            title = web_content.split("\"clip(this)\">")[1].split("<i>")[1].\
                split('.')[0]
        except:
            title = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        
        if doi not in self._doi_collection:
            self._doi_collection.append(doi)
            self._title_collection.append(title)

            start_index = web_content.index("location.href=\'") + 15
            end_index = web_content[start_index+1:].index("'")+start_index+1
            cur_pdf_url = web_content[start_index:end_index]
            if "https:" not in cur_pdf_url:
                cur_pdf_url = "https:" + cur_pdf_url
            self._url_collection.append(cur_pdf_url)
        else:
            warnings.warn("This paper already exists in the queue!")


    def _get_url_search(self, url):
        '''
        search DOI given Google Scholar pages
        '''
        r = requests.get(url, headers = self.headers)
        web_content = r.content.decode('utf-8', errors='replace')
        loc_list = web_content.split("doi/abs")[1:]
        for item in loc_list:
            self.input_article(item[1:item.index("\"")])


    def cur_articles(self):
        '''
        print current DOIs
        '''
        print("Currently stored articles:")
        print("------------------------")
        print("{:<10} {:<20} {:<1}".format('Index', 'DOI', 'Title'))
        for i in range(len(self._doi_collection)):
            print("{:<5} {:<20} {:<1}".format(i + 1, self._doi_collection[i], self._title_collection[i]))
        print("------------------------")
        print("Total of %d articles" %len(self._doi_collection))


    def remove_article(self):
        '''
        remove DOIs by index
        '''
        print("Enter index needed to be removed, press 0 to exit")
        while True:
            self.cur_articles()
            index = input()
            assert index.isdigit(), "Please input a number!"
            index = int(index)
            if not index:
                break
            self._doi_collection.pop(index - 1)
            self._url_collection.pop(index - 1)
            self._title_collection.pop(index - 1)
            if len(self._doi_collection) == 0:
                print("Queue is empty!")
                break


    def input_article(self, doi):
        '''
        input DOI or website address
        '''
        url = self.SCIHUB + doi
        self._get_url_doi(url)


    def search(self, search, num_of_page = 1):
        '''
        input keywords
        '''
        if not search:
            raise ValueError("Please input title/keyword/author!")

        search = "+".join(re.sub(r'[^\w\s]', ' ', search).split())
        url = self.SCHOLAR + search
        for i in range(0, num_of_page):
            self._get_url_search(url[:41] + str(i-1) + url[41:])


    def download(self, direction=None):
        '''
        download articles in the queue. 
        '''
        if not self._url_collection:
            raise ValueError("Queue is empty!")
        
        if not direction:
            try:
                direction = open("%s/.getarticle.ini" %expanduser("~"), \
                    "rb").read().decode()
            except:
                direction = '.'

        print("Downloading %d papers" %len(self._url_collection))
        while self._url_collection:
            url = self._url_collection.pop(0)
            doi = self._doi_collection.pop(0)
            title = self._title_collection.pop(0)
            print(doi, title)
            article = requests.get(url, allow_redirects=True).content
            open("%s/%s.pdf" %(direction, title), 'wb').write(article)
