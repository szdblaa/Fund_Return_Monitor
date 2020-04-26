# -*- coding: utf-8 -*-
import scrapy
from fund_spider.items import FundSpiderItem

class TtjijinSpider(scrapy.Spider):
    name = 'ttjijin'
    allowed_domains = ['http://fund.eastmoney.com/']
#    需要爬取的基金网址列表
    start_urls = ['http://fund.eastmoney.com/540006.html',
                  'http://fund.eastmoney.com/519066.html']

        
    def parse(self, response):
        net_worth = response.xpath("//*[@id=\"body\"]/div[12]/div/div/div[2]/div[1]/div[1]/dl[2]/dd[1]/span[1]/text()").extract()
#        519006这只基的基金代码取法
        fund_number=response.xpath("//*[@id=\"body\"]/div[12]/div/div/div[1]/div[1]/div/span[2]/span[1]/text()").extract()
#        519066这个基金比较特殊，前后端基金代码不同，故做此处理
        if fund_number==[]:
#            判断是否为519066，为空则认为不是，采用一般基金的取法，如下
           fund_number=response.xpath("//*[@id=\"body\"]/div[12]/div/div/div[1]/div[1]/div/span[2]/text()").extract()
        item=FundSpiderItem()
        item['net_worth']=net_worth
        item['fund_number']=fund_number
        yield item


