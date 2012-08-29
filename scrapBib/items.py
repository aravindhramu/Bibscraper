# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapbibItem(Item):
    # define the fields for your item here like:
    # name = Field()
    bookname = Field()
    price = Field()
    bookstore = Field()
