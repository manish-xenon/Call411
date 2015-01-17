# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors

class Call411Pipeline(object):

    def __init__(self):
        self.dbPool = adbapi.ConnectionPool('MySQLdb', db='call411', user='call411', passwd='cs411', cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        query = self.dbPool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute("select * from phones where model_number = %s", (item['model_number']))
        result = tx.fetchone()
        if result:
#           log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
#            print 'Item already stored in db: {0}'.format(item)
            pass
        else:
            assert(type(item['ram']) is int)
            assert(type(item['battery_capacity']) is int)
            assert(type(item['price']) is int)
            assert(type(item['screen_size']) is float or type(item['screen_size']) is int)
            assert(type(item['talk_time']) is float or type(item['talk_time']) is int)
            assert(type(item['camera_mp']) is float or type(item['camera_mp']) is int)
            tx.execute(\
                "insert into phones (model_number, ram, processor, manufacturer, system, screen_size, screen_resolution, battery_capacity, talk_time, camera_megapixels, price, weight, storage_options, dimensions, carrier, network_frequencies, image) "
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item['model_number'], item['ram'], item['cpu'], item['manufacturer'], item['os'], item['screen_size'], item['screen_resolution'], item['battery_capacity'], item['talk_time'], item['camera_mp'], item['price'], item['weight'], item['storage'], item['dimensions'], None, None, item['image'])
            )
#           log.msg("Item stored in db: %s" % item, level=log.DEBUG)
#            print 'Item stored in db: {0}'.format(item)

    def handle_error(self, e):
#       log.err(e)
        print e
