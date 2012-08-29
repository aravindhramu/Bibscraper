from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapBib.items import *
import re

class HSSpider(CrawlSpider):
    name = "homeshopspider"
    allowed_domains = ["homeshop18.com"]

    def __init__(self,*args,**kwargs):
        super(HSSpider,self).__init__(*args,**kwargs)
        isbn = kwargs.get('isbn')
        self.start_urls = ["http://www.homeshop18.com/"+isbn+"/search:"+isbn]

    def parse(self,response):
        hls = HtmlXPathSelector(response)
        it = ScrapbibItem()
        bkname = hls.select('//div[@class="listView_title"]/a[@title]/text()').extract()
        it['bookname'] = bkname
        price = hls.select('//span[@class="our_price"]/text()').extract()
        it['price'] = price
        it['bookstore'] = self.allowed_domains[0]
        return it
