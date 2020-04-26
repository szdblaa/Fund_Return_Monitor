#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:43:14 2020
基金收益率监控程序的主程序


@author: szdbl
"""
#import os
#from scrapy import cmdline


import fund_generator.fund_generator as ffg
import fund_calculator.fund_calculator as frc
import fund_writer.fund_writer as frw
import fund_notice.fund_notice as frn
import fund_twilio.fund_twilio as frt

#定义各目录
fund_trad_file_dir='/Users/szdbl/Documents/基金收益率监控/基金交易/'
fund_share_file_dir='/Users/szdbl/Documents/基金收益率监控/基金份数/'
fund_xirr_file_dir='/Users/szdbl/Documents/基金收益率监控/基金xirr收益/'


  
#实例化文件生成类
ffg_instance=ffg.Fund_File_Generator(fund_trad_file_dir)


#计算每个基金的xirr，并写入fund_xirr_txt_dir文件
message=[]
for fund_number in ffg_instance.file_name():
    #存放短信内容  
    #声明基金交易、基金份额、基金xirr收益文件的路径
    fund_trad_txt_dir=fund_trad_file_dir+fund_number+'.txt'
    fund_share_txt_dir=fund_share_file_dir+fund_number+'.txt'
    fund_xirr_txt_dir=fund_xirr_file_dir+fund_number+'.txt'
    #实例化基金总额，xirr收益率计算模块类
    frc_instance=frc.Fund_Return_Calculator(fund_trad_txt_dir,fund_share_txt_dir)
    #计算基金总额和xirr收益率
    fund_worth,fund_xirr=frc_instance.fund_return(fund_trad_txt_dir)
    #实例化告警模块
    frn_instance=frn.Fund_Return_Notice(fund_number,fund_worth,fund_xirr)
    if not frn_instance.fund_notice():
        continue
    else:
        message.append(frn_instance.fund_notice())
    #持久化模块
    frw_instance=frw.Fund_Return_Writer(fund_xirr_txt_dir,fund_worth,fund_xirr)
    frw_instance.fund_write()
if message==[]:
    message=['今日基金无事，退朝~']
#    发短信模块
text='基金,总额,收益率\n'+"\n".join(message)
frt_instance=frt.Fund_Return_Twilio(text)
frt_instance.fund_twilio()
#print(message)


        