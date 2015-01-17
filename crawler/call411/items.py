# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PhoneItem(scrapy.Item):
    # define the fields for your item here like:
	name = scrapy.Field()
	ram = scrapy.Field()
	cpu = scrapy.Field()
	manufacturer = scrapy.Field()
	os = scrapy.Field()
	screen_size = scrapy.Field()
	model_number = scrapy.Field()
	screen_resolution = scrapy.Field()
	battery_capacity = scrapy.Field()
	talk_time = scrapy.Field()
	camera_mp = scrapy.Field()
	price = scrapy.Field()
	weight = scrapy.Field()
	storage = scrapy.Field()
	dimensions = scrapy.Field()
	carrier = scrapy.Field()
	network_freq = scrapy.Field()
	image = scrapy.Field()
	pass
