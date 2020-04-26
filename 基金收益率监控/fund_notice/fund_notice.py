#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:09:39 2020
基金收益率监控程序-告警模块
@author: szdbl
"""

class Fund_Return_Notice(object):
    #将date,money,xirr写入xirr_txt_dir文件
    def __init__(self,fund_number,fund_worth,fund_xirr): 
        self.fund_number = fund_number# int(fund_number)
        self.fund_worth = float(list(fund_worth)[1])
        self.fund_xirr = float(fund_xirr)
                               
    #预警规则模块：
    #收益率超过15%或基金池大于50000
    def warn_rule(self):
        if self.fund_worth>=50000 or self.fund_xirr>=0.15:
            return True
        else:
            return False
    
    def fund_notice(self):
        if self.warn_rule():
             return str(self.fund_number)+','+str(self.fund_worth)+','+str(self.fund_xirr)#+'\n'   

    
        