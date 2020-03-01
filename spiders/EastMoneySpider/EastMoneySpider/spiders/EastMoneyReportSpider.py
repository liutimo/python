# -*- coding: utf-8 -*-
import scrapy


class EastmoneyreportspiderSpider(scrapy.Spider):
    name = 'EastMoneyReportSpider'
    allowed_domains = ['data.eastmoney.com']
    start_urls = ['http://data.eastmoney.com/report/industry.jshtml']

    def parse(self, response):
        print(response.body)
        pass
