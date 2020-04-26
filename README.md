# Fund_Return_Monitor
基金收益率监控

项目背景：

我在天天基金app上投了几个基金，但没空每天登录查看收益率，以便及时进行交易操作。																										

所以此项目就是为了实现：

1、利用爬虫自动爬取基金网站数据，保存到本地文件

2、计算各基金收益率，如达到预定的阈值则短信提醒及时交易

脚本说明：

fund_monitor.sh:每天定时跑的脚本

fund_spider:爬虫模块

fund_generator:文件生成模块

fund_calculator:收益率计算模块

fund_notice:阈值及告警内容设置模块

fund_writer:数持久化模块

fund_twilio:短信通知模块

基金份数:一个基金一个txt文件，格式：date,share,net_worth

基金交易:一个基金一个txt文件，格式：date,money

