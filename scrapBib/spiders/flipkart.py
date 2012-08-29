from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapBib.items import *
import re

class FKSpider(CrawlSpider):
    name = "flipkartspider"
    allowed_domains = ["flipkart.com"]

    def __init__(self,*args,**kwargs):
        super(FKSpider,self).__init__(*args,**kwargs)
        isbn = kwargs.get('isbn')
        self.start_urls = ["http://www.flipkart.com/search/a/all?query="+isbn]

    def parse(self,response):
        hls = HtmlXPathSelector(response)
        it = ScrapbibItem()
        bkname = hls.select('//title/text()').extract()
        it['bookname'] = bkname
        price = hls.select('//span[@class="price list price-td"]/text()').extract() 
        it['price'] = price
        it['bookstore'] = self.allowed_domains[0]
        return it

