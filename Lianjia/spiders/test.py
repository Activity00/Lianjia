#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月24日

@author: 武明辉
'''
import scrapy


class TestSpider(scrapy.Spider):
    name='test'
    start_urls=['http://localhost:8000/fa']
    
    def parse(self, response):
        a=response.xpath(u'//a[contains(text(),"帮助")]/@href').extract_first()
        print a
        