#-*-coding:utf-8-*-
#！usr/bin/env python
'''
Created on 2017年2月28日

@author: 武明辉
'''
import scrapy


class GetIps(scrapy.Spider):
    name='getips'
    start_urls=['http://www.xicidaili.com/nn/']
    
    def parse(self, response):
        pass
    
    
    