import scrapy

from bs4 import BeautifulSoup
from googlePatent.items import GooglepatentItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class patentCrawler(CrawlSpider):
    name = 'googlePatent'
    url_num = '6923000'

    title_list = []
    abstract_list = []
    content_list = []
        
    while int(url_num) < 6923100:
    
        start_urls = ['http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=' + url_num + '.PN.&OS=PN/' + url_num + '&RS=PN/' + url_num]
        
        def parse(self, response):
            res = BeautifulSoup(response.body)
            
            for titles in res.select('body'):
                title_list.append(titles.select('font')[0].text)
            for abstracts in res.select('body'):
                abstract_list.append(abstracts.select('p')[0].text)
            for contents in res.select('body'):
                content_list.append(contents.select('coma')[0].text)

            googlepatentitem = GooglepatentItem()
            googlepatentitem['title'] = title_list
            googlepatentitem['abstract'] = abstract_list
            googlepatentitem['content'] = content_list
            return googlepatentitem
            
        url_num = str(int(url_num) + 1)
