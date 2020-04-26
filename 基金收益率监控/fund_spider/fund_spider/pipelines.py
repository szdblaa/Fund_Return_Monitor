# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
today=datetime.date.today()
today=str(today)



class FundSpiderPipeline(object):
    def process_item(self, item, spider):
        net_worth=item['net_worth']
        fund_number=item['fund_number']
        net_worth=net_worth[0]
        fund_number=fund_number[0]
        with open('/Users/szdbl/Documents/基金收益率监控/基金份数/{}.txt'.format(fund_number),'a+') as f:
#            f.write('date,share,net_worth\n')
            f.write(today)
            f.write(',,')
            f.write(net_worth)   
            f.write('\n')
        return item
