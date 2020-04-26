#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:58:42 2020
基金收益率监控程序-持久化模块
@author: szdbl
"""
import os

class Fund_Return_Writer(object):
    #将date,money,xirr写入xirr_txt_dir文件
    def __init__(self,xirr_txt_dir,fund_worth,fund_xirr): 
        self.xirr_txt_dir = xirr_txt_dir
        self.fund_worth = fund_worth
        self.fund_xirr = fund_xirr
        
    #将date,money,xirr写入xirr_txt_dir文件
    def fund_write(self):
    #with open():当文件不存在则新建空文件，否则直接打开 
        with open(self.xirr_txt_dir,'a+') as f:
    #文件若为空，则先写入标题行
            if os.path.getsize(self.xirr_txt_dir)==0:
                f.write("date,money,xirr\n")
    #date
            f.write(str(self.fund_worth[0]))
            f.write(',')
    #money
            f.write(str(self.fund_worth[1]))
            f.write(',')
    #xirr值
            f.write(str(round(self.fund_xirr,4)))
            f.write('\n')