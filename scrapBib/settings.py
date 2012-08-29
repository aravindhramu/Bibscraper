# Scrapy settings for scrapBib project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapBib'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrapBib.spiders']
NEWSPIDER_MODULE = 'scrapBib.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['scrapBib.pipelines.ScrapbibPipeline']
