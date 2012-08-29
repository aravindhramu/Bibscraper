Bibscraper
==========


Bibscraper helps to conveniently compare price of a book by giving its isbn across multiple e-bookstores.
Currently, in the first cut only flipkart,infibeam and homeshop18 have been added.

This project is based on scrapy module in python.

To use it navigate inside scrapBib folder and type:

scrapy crawl crawler_name -a isbn=isbn_number

crawler names are defined inside scrapBib/spiders/ in their respective .py files.

Results are pipelined in  json format to results.out. This file will be created
in the same folder you execute the command.

UI will be added soon.

Any comments/suggestions are welcome. Mail me at aravindhramu@gmail.com

