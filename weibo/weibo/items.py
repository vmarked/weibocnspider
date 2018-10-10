# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义了collection字段, 指明保存的名称


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'weibos'
    id = scrapy.Field()
    attitudes_count = scrapy.Field()
    comments_count = scrapy.Field()
    reposts_count = scrapy.Field()
    picture = scrapy.Field()
    pictures = scrapy.Field()
    source = scrapy.Field()
    text = scrapy.Field()
    raw_text = scrapy.Field()
    thumbnail = scrapy.Field()
    user = scrapy.Field()
    created_at = scrapy.Field()
    crawled_at = scrapy.Field()


class UserItem(scrapy.Item):
    collection = 'users'
    id = scrapy.Field()
    name = scrapy.Field()
    avatar = scrapy.Field()
    cover = scrapy.Field()
    gender = scrapy.Field()
    description = scrapy.Field()
    fans_count = scrapy.Field()
    follows_count = scrapy.Field()
    weibos_count = scrapy.Field()
    verified = scrapy.Field()
    verified_reason = scrapy.Field()
    verified_typa = scrapy.Field()
    follows = scrapy.Field()
    fans = scrapy.Field()
    crawled_at = scrapy.Field()


# 用户关注和粉丝列表
class UserRelationItem(scrapy.Item):
    collection = 'users'
    id = scrapy.Field()  # 用户ID
    follows = scrapy.Field()  # 关注列表
    fans = scrapy.Field()  # 粉丝列表
