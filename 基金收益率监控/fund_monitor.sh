
#爬虫模块存放的路径
cd /Users/szdbl/Documents/基金收益率监控/fund_spider

scrapy crawl ttjijin -s LOG_FILE=spider_message.log

rm ./spider_message.log

#基金收益率监控主程序存放的路径
cd /Users/szdbl/Documents/基金收益率监控

python main.py
