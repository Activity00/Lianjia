# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    title=scrapy.Field()#标签
    community=scrapy.Field()#小区
    model=scrapy.Field()#户型
    floor=scrapy.Field()#楼层
    orientation=scrapy.Field()#朝向
    decorate=scrapy.Field()#装修程度
    buildtime=scrapy.Field()#时间/类型
    area=scrapy.Field()#面积
    focus_num=scrapy.Field()#关注人数
    watch_num=scrapy.Field()#观看人数
    time=scrapy.Field()#发布时间
    price=scrapy.Field()#价格
    link=scrapy.Field()#详细链接
    Latitude=scrapy.Field()#金维度
    city=scrapy.Field()#城区
    