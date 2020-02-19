# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector

class MoneySpiderSpider(scrapy.Spider):
    # name = 'money_spider'
    name = 'myspider'
    # name = 'money163'
    allowed_domains = ['money.163.com']
    start_urls = ['http://money.163.com/', 'http://money.163.com/stock/']

    rules = Rule(
       LinkExtractor(allow=r"/\d+/\d+/\d+/*"),
       follow=True,
       callback="moneyparser"
    )

    def moneyparser(self,response):
       item = MoneyNewsItem()
       title = response.xpath("/html/head/title/text()").extract()
       if title:
          item['news_title'] = title[0][:-5]

       news_url = response.url
       if news_url:
          item['news_url'] = news_url

       news_body = response.xpath("//div[@id='endText']/p/text()").extract()
       if news_body:
          item['news_body'] = news_body
