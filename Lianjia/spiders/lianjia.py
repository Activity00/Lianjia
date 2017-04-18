#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月23日

@author: 武明辉
'''
from time import sleep
import time

import scrapy

from Lianjia.items import LianjiaItem


class Lianjia(scrapy.Spider):
    name='lianjia'
    start_urls=['http://bj.lianjia.com/ershoufang/']
    
    def parse(self, response):
        print response.body
        positions=response.xpath('//div[@data-role="ershoufang"]/div/a/@href').extract()
        for position in positions:
            yield scrapy.Request(response.urljoin(position),self.parselist)
    
    def parselist(self,response):
        listurls=response.xpath('//li[@class="clear"]/a/@href').extract()
        for liurl in listurls:
            yield scrapy.Request(liurl,self.parseDetail)
        next_page=response.xpath(u'//div[@class="page-box house-lst-page-box"]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
            
        
    def parseDetail(self,response):
        item=LianjiaItem()
        item['title']=response.xpath('//div[@class="title"]/h1/text()').extract_first()
        item['community']=response.xpath('//div[@class="communityName"]/a[@class="info"]/text()').extract_first()
        item['model']=response.xpath('//div[@class="room"]/div[@class="mainInfo"]/text()').extract_first()#户型
        item['floor']=response.xpath('//div[@class="room"]/div[@class="subInfo"]/text()').extract_first()
        item['orientation']=response.xpath('//div[@class="type"]/div[@class="mainInfo"]/text()').extract_first()
        item['decorate']=response.xpath('//div[@class="type"]/div[@class="subInfo"]/text()').extract_first()
        item['area']=response.xpath('//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first()#面积
        item['buildtime']=response.xpath('//div[@class="area"]/div[@class="subInfo"]/text()').extract_first()
        item['focus_num']=response.xpath('//span[@id="favCount"]/text()').extract_first()#关注人数
        item['watch_num']=response.xpath('//span[@id="cartCount"]/text()').extract_first()#观看人数
        item['time']=response.xpath('//div[@class="transaction"]//ul/li[1]/text()').extract_first()#发布时间
        item['price']=response.xpath('//span[@class="total"]/text()').extract_first()#价格
        item['link']=response.url#详细链接
        item['Latitude']=response.xpath('//script[19]/text()').re_first(r"resblockPosition:'(.*?)'")#金维度
        item['city']=response.xpath('//span[@class="info"]/a[1]/text()').extract_first()#城区
        yield item
    
    