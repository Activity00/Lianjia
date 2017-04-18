# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
import random

from Lianjia.settings import PROXIES


# class LianjiaSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
# 
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
# 
#     def process_spider_input(response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
# 
#         # Should return None or raise an exception.
#         return None
# 
#     def process_spider_output(response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
# 
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
# 
#     def process_spider_exception(response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
# 
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
# 
#     def process_start_requests(start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
# 
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
# 
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    '''动态切换user-agent'''
    def __init__(self,agents):
        self.agents=agents
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))

    
class ProxyMiddleware(object):
    '''动态切换ip'''
    def process_request(self, request, spider):  
        proxy = random.choice(PROXIES)  
        if proxy['user_pass'] is not None:  
            request.meta['proxy'] = "http://%s" % proxy['ip_port']  
            encoded_user_pass = base64.encodestring(proxy['user_pass'])  
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass  
            print "**************ProxyMiddleware have pass************" + proxy['ip_port']  
        else:  
            print "**************ProxyMiddleware no pass************" + proxy['ip_port']  
            request.meta['proxy'] = "http://%s" % proxy['ip_port'] 
    
aaa='''lianjia_uuid=86779b08-9e44-455d-a72c-fce788a844dd; CNZZDATA1253477573=1661847726-1488245711-http%253A
%252F%252Fcaptcha.lianjia.com%252F%7C1488353724; _jzqa=1.3530497733104389600.1488249979.1488249979.1488357370
.2; _jzqx=1.1488249979.1488357370.1.jzqsr=captcha%2Elianjia%2Ecom|jzqct=/.-; CNZZDATA1254525948=732224810-1488249188-http
%253A%252F%252Fcaptcha.lianjia.com%252F%7C1488357195; CNZZDATA1255633284=136098194-1488248160-http%253A
%252F%252Fcaptcha.lianjia.com%252F%7C1488356162; CNZZDATA1255604082=693772193-1488244902-http%253A%252F
%252Fcaptcha.lianjia.com%252F%7C1488352904; _qzja=1.771347262.1488249979255.1488249979255.1488357369883
.1488249984811.1488357369883.0.0.0.3.2; _smt_uid=58b4e47b.4f9b7796; _ga=GA1.2.1139743737.1488249983;
 lianjia_ssid=666e9a40-d21d-4f45-a532-01b72c67d5cc; select_city=110000; sample_traffic_test=controlled_61
; all-lj=144beda729446a2e2a6860f39454058b; _jzqb=1.1.10.1488357370.1; _jzqc=1; _jzqckmp=1; _qzjb=1.1488357369883
.1.0.0.0; _qzjc=1; _qzjto=1.1.0; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent
=1'''   
class CookieMiddleware(object):
    
    def process_request(self, request, spider):
        request.meta['Cookie']=self.stringToDict(aaa)
        print 'aaa'
    def stringToDict(self,cookiestr):
        itemDict = {}
        items = cookiestr.split(';')
        for item in items:
            key = item.split('=')[0]
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict 

class ProxytxtMiddleware(object):
    '''动态切换ip'''
    def __init__(self):
        self.lins=open('ipn.txt','r').readlines()
        print self.lins
        self.totalpage=len(self.lins)
        self.index=0
    def process_request(self, request, spider):  
        proxy = self.lins[self.index]
        if self.index<self.totalpage-1:
            self.index+=1
        else:
            self.index=0
        if proxy is not None:
            print 'use:',proxy  
            request.meta['proxy'] = "http://%s" % proxy

   