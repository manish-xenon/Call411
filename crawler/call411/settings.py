# -*- coding: utf-8 -*-

# Scrapy settings for call411 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'call411'

SPIDER_MODULES = ['call411.spiders']
ITEM_PIPELINES = {
	'call411.pipelines.Call411Pipeline': 100
}
NEWSPIDER_MODULE = 'call411.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'call411 (+http://www.yourdomain.com)'
