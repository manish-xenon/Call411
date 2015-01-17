from twisted.enterprise import adbapi
import MySQLdb.cursors
from phones.models import Phone

class PhoneQuery:

    def __init__(self):
        self.dbPool = adbapi.ConnectionPool('MySQLdb', db='call411', user='call411', passwd='cs411', cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)

    def insert(self, phone):
        query = self.dbPool.runInteraction(self._conditional_insert, phone)
        query.addErrback(self.handle_error)

    def select(self, phone):
        query = None
        if phone is None:
            query = self.dbPool.runInteraction(self._select_all)
        else:
            query = self.dbPool.runInteraction(self._select_phone, phone)
        query.addErrback(self.handle_error)

    def delete(self, phone):
        query = self.dbPool.runInteraction(self._delete, phone)
        query.addErrback(self.handle_error)
        
    def delete_by_model_num(self, model_num):
        query = self.dbPool.runInteraction(self._delete_md, model_num)
        query.addErrback(self.handle_error)
    
    def _conditional_insert(self, tx, phone):
        tx.execute("select * from phones where model_number = %s", (phone.model_number))
        result = tx.fetchone()
        if result:
            tx.execute("update phones set ram={0}, processor={1}, manufacturer={2}, system={3}, screen_size={4} where model_number={5}".format(phone.ram, phone.processor, phone.manufacturer, phone.system, phone.screen_size, phone.model_number))
            print 'Item updated in db'
        else:
            tx.execute(\
                "insert into phones (model_number, ram, processor, manufacturer, system, screen_size) "
                "values (%s, %s, %s, %s, %s, %s)",
                (phone.model_number, phone.ram, phone.processor, phone.manufacturer, phone.system, phone.screen_size)
            )
            print 'Item stored in db'
    
    def _delete(self, tx, phone):
        try:
            tx.execute("delete from phones where model_number=%s" % phone.model_number)
        except:
            return
            
    def _delete_md(self, tx, model_num):
        try:
            tx.execute("delete from phones where model_number=%s" % model_num)
        except:
            return
            
    def _select_all(self, tx):
        tx.execute("select * from phones")
        return tx.fetchall()

    def _select_model(self, tx, phone):
        tx.execute("select * from phones where model_number = %s" % phone.model_number)
        return tx.fetchone()
    
    def handle_error(self, e):
        print e
