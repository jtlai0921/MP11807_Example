# -*- coding: utf-8 -*-
import scrapy

class ExampleSpider(Spider):
   name = "stocknews"

   def __init__(self, site='money.163.com', *args, **kwargs):
      allowrule = r"/\d+/\d+/\d+/*"
      self.counter = 0
      self.stock_id = id
      self.allowed_domain=[site]
      self.start_urls = ['http://\%s' \% (site)]

      super(ExampleSpider, self).__init__(*args, **kwargs)

      # allowrule = "/\%s/\%s\%s/\d+/*" \% (year, month, day)
      # ExampleSpider.rules=(Rule(LinkExtractor(allow=allowrule), callback="parse_news", follow=True),)

