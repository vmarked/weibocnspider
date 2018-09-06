# -*- coding: utf-8 -*-
import scrapy


class WeibocnSpider(scrapy.Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['http://m.weibo.cn/']
    # 用户页面API
    # user_url = "https://m.weibo.cn/profile/{uid}"
    # user_url = "https://m.weibo.cn/u/{uid}?uid={uid}&luicode=10000011&lfid=230413{uid}"
    user_url = "https://m.weibo.cn/profile/info?uid={uid}"
    # 关注页面API
    follow_url = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}"
    # 粉丝页面API
    fan_url = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&since_id={page}"
    # 微博列表API
    weibo_url = "https://m.weibo.cn/api/container/getIndex?containerid=230413{uid}&page_type=03&page={page}"
    # 用户列表['中国日报', '人民日报', '中国长安网', '中国青年报', '局面']
    start_users = ['1663072851', '2803301701', '5617030362', '1726918143', '6294930327']

    def start_requests(self):
        for uid in self.start_users:
            yield scrapy.Request(self.user_url.format(uid=uid), callback=self.parse_user)

    def parse_user(self, response):
        """
        解析用户信息
        :param response: Response对象
        :return:
        """
        pass

    def parse_follows(self, response):
        """
        解析用户关注
        :param response: Response对象
        :return:
        """
        pass

    def parse_fans(self, response):
        """
        解析用户粉丝
        :param response: Response对象
        :return:
        """
        pass

    def parse_weibos(self, response):
        """
        解析用户微博列表
        :param response: Response对象
        :return:
        """
        pass
