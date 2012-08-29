from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapBib.items import *
import re

class IBSpider(CrawlSpider):
    name = "infibeamspider"
    allowed_domains = ["infibeam.com"]

    def __init__(self,*args,**kwargs):
        super(IBSpider,self).__init__(*args,**kwargs)
        isbn = kwargs.get('isbn')
        self.start_urls = ["http://www.infibeam.com/search?q="+isbn]

    def parse(self,response):
        hls = HtmlXPathSelector(response)
        it = ScrapbibItem()
        bkname = hls.select('//div[@class="boxinner big"]/ul/li/a[@title]/span[@class="showcaseTitle"]/text()').extract()
        it['bookname'] = bkname
        price = hls.select('//div[@class="boxinner big"]/ul/li/div[@class="price"]/span[@class="normal"]/text()').extract()
        it['price'] = price
        it['bookstore'] = self.allowed_domains[0]
        return it
