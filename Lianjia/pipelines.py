# -*- coding: utf-8 -*-
import MySQLdb
import datetime


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class LianjiaPipeline(object):
    def __init__(self, db_uri,db_name,username,password):
        self.db_uri = db_uri
        self.db_name = db_name
        self.username=username
        self.password=password
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_uri=crawler.settings.get('DB_URI'),
            db_name=crawler.settings.get('DB_NAME', 'lianjia'),
            username=crawler.settings.get('DB_USERNAME'),
            password=crawler.settings.get('DB_PASSWORD') 
        )
    def open_spider(self, spider):
        self.db = MySQLdb.connect(self.db_uri,self.username,self.password,self.db_name,charset="utf8")
        
    def close_spider(self, spider):
        self.db.close()
    
    def process_item(self, item, spider):
        print '开始存',item
        time=datetime.datetime.strptime(item['time'],'%Y-%m-%d').date()
        cursor = self.db.cursor()
        try:
            cursor.execute('select title,community,model,buildtime from lianjia')
            r=cursor.fetchone()
            if r==(item['title'],item['community'],item['model'],item['buildtime']):
                print '丢掉一个存在的数据'
                return item
            cursor.execute('insert into lianjia(title,community,model,floor,orientation,decorate,buildtime,area,focus_num,watch_num,time,price,link,Latitude,city) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
            item['title'],item['community'],item['model'],item['floor'],item['orientation'],item['decorate'],item['buildtime'],item['area'],item['focus_num'],item['watch_num'],time,item['price'],item['link'],item.get('Latitude','0'),item['city']))
            self.db.commit()
        except Exception as e:
            print '数据库存储错误',e
            self.db.rollback()
        return item
