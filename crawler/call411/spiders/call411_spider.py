import scrapy
import json
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from call411.items import PhoneItem
from decimal import Decimal

class Call411Spider(CrawlSpider):
    name = 'call411'
    allowed_domains = ['phonearena.com']
    start_urls = [
        'http://www.phonearena.com/phones'
    ]
    rules = (
        Rule(LinkExtractor(allow=('(phones[/][a-zA-Z0-9-]+_id)[0-9]+'), unique=True), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=('([/]phones[/]page[/])[0-9]+'), unique=True), callback='parse_page', follow=True),
    )

    def parse_item(self, response):
        phone = PhoneItem()

        name = response.xpath("//div[@id='phone']/h1/span/text()").extract()
        phone['name'] = name[0] if len(name) > 0 else ""

        sysmem = response.xpath("//ul/li[strong/span/text()='System memory:']/ul/li/text()").extract()
        ram = sysmem[0] if len(sysmem) > 0 else None 
        phone['ram'] = ram.partition(' / ')[0] if ram is not None else None
        phone['ram'] = int(phone['ram'].partition(' ')[0]) if phone['ram'] is not None else -1 

        cpu = response.xpath("//ul/li[strong/span/text()='System chip:']/ul/li/text()").extract()
        phone['cpu'] = cpu[0] if len(cpu) > 0 else None 

        phone['manufacturer'] = phone['name'].split()[0] if len(phone['name']) > 0 else None 

        os = response.xpath("//ul/li[strong/text()='OS:']/ul/li/text()").extract()
        phone['os'] = os[0] if len(os) > 0 else None

        display = response.xpath("//ul/li[strong/text()='Physical size:']/ul/li/text()").extract()
        phone['screen_size'] = display[0] if len(display) > 0 else None 
        phone['screen_size'] = float(phone['screen_size'].partition(' ')[0]) if phone['screen_size'] is not None else -1 

        phone['model_number'] = phone['name']

        res = response.xpath("//ul/li[strong[@class=' s_lv_1 ']/text()='Resolution:']/ul/li/text()").extract()
        phone['screen_resolution'] = res[0] if len(res) > 0 else None 

        battery = response.xpath("//ul/li[strong/text()='Capacity:']/ul/li/text()").extract() 
        phone['battery_capacity'] = battery[0] if len(battery) > 0 else None 
        phone['battery_capacity'] = int(phone['battery_capacity'].partition(' ')[0]) if phone['battery_capacity'] is not None else -1 

        talk_time = response.xpath("//ul/li[strong/text()='Talk time:']/ul/li/text()").extract() 
        phone['talk_time'] = talk_time[0] if len(talk_time) > 0 else None 
        phone['talk_time'] = float(phone['talk_time'].partition(' ')[0]) * 60 if phone['talk_time'] is not None else -1 

        camera_mp = response.xpath("//ul/li[strong[@class=' s_lv_1 ']/text()='Camera:']/ul/li/ul/li/text()").extract()
        phone['camera_mp'] = camera_mp[0] if len(camera_mp) > 0 else None 
        try:
            phone['camera_mp'] = float(phone['camera_mp'].partition(' ')[0]) if phone['camera_mp'] is not None else -1
        except:
            phone['camera_mp'] = -1

        price = response.xpath("//ul/li[strong/text()='MSRP price:']/ul/li/text()").extract()
        phone['price'] = price[0] if len(price) > 0 else None
        phone['price'] = int(phone['price'].split(' ')[1]) if phone['price'] is not None else -1

        weight = response.xpath("//ul/li[strong/text()='Weight:']/ul/li/text()").extract()
        phone['weight'] = weight[0] if len(weight) > 0 else None 
        phone['weight'] = float(phone['weight'].partition(' ')[0]) if phone['weight'] is not None else -1

        storage = response.xpath("//ul/li[strong/text()='Built-in storage:']/ul/li/text()").extract()
        phone['storage'] = storage[0] if len(storage) > 0 else None 

        dimensions = response.xpath("//ul/li[strong/text()='Dimensions:']/ul/li/text()").extract()
        phone['dimensions'] = dimensions[0] if len(dimensions) > 0 else None 

        carrier = response.xpath("//div[@class='carriers']/a/text()").extract()
        phone['carrier'] = carrier

        phone['network_freq'] = None

        image_link = response.xpath("//div[@class='lcimg']/a/@href").extract()
        phone['image'] = 'http:%s' % image_link[0] if len(image_link) > 0 else None 

        if phone['model_number'] == '' or phone['model_number'] is None:
            print 'Dropping {0} ({1})'.format(response.url, response.xpath("//div[@id='phone']/h1/span/text()"))
            return None
        return phone

    def parse_page(self, response):
        print 'Page ' + response.url
