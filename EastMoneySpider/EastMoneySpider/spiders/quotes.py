# -*- coding: utf-8 -*-
import scrapy
from EastMoneySpider.items import EastmoneyspiderItem

class TestSpider(scrapy.Spider):
    name = 'quotes'                     #标识一个爬虫，项目内唯一

    # 如果定义了start_urls,就可以不重载start_requests。重载的目的是向请求中加入一些参数。
    #start_urls = ['https://blog.csdn.net/weixin_44274975/article/details/88362819',]

  
    #必须返回一个关于scrapy.Request的可迭代对象[generator function、list]
    def start_requests(self):
        item = EastmoneyspiderItem(name = "lz")
        print(item['name'])
        pass
        urls = [
                'http://quotes.toscrape.com/page/1/',
            ]
        for url in urls:
            yield scrapy.Request(url, self.parse)

    # 处理response。The response parameter is an instance of TextResponse that holds the page  
    # content and has further helpful methods to handle it.
    # The parse() method usually parses the response, extracting the scraped data as dicts and also 
    # finding new URLs to follow and creating new requests (Request) from them.
    def parse(self, response):
        # self.saveResponse(response)
        for quote in response.css('div.quote'):
            yield {
                'text' : quote.css('span.text::text').get(),
                'author' : quote.css('small.author::text').get(),
                'tags' : quote.css('div.tags a.tag::text').getall(),
            }

        # next_page = response.css('ul.pager li.next a').attrib['href']  #这种方式不好，当找不到href时，会报异常
        # next_page = response.css('li.next a::attr(href)').get()  # next_page type is str
        # if next_page is not None:
        #     # urljoin 拼接url
        #     # next_page = response.urljoin(next_page)
        #     # print(next_page)
        #     # 1
        #     # yield scrapy.Request(next_page, self.parse)
        #     # 2
        #     # yield response.follow(next_page, self.parse)  #返回scrapy.Request so，need to yield

        #     # 1 和 2 的区别
        #     # 后者直接支持相对路径，前者需要urljoin拼接

        # We can pass a selector to response follow

        # yield response.follow(next_page, self.parse)
        # for href in response.css('li.next a::attr(href)'):
        #     # href type is selector
        #     yield response.follow(href, self.parse)

        # use a element directly
        for a in response.css('li.next a'):
            # a type is Selector
            yield response.follow(a, self.parse)

    def saveResponse(self, response):
        filename = "%s.html" % response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

