#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:27:35 2020
基金收益率监控程序-基金总额，xirr收益率计算模块
@author: szdbl
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:42:47 2020

@author: szdbl
"""

#import datetime as datetime
from datetime import datetime as datetime2
import fund_calculator.xirr as xirr



class Fund_Return_Calculator(object):
    def __init__(self,trad_txt_dir,share_txt_dir): 
        self.trad_txt_dir = trad_txt_dir
        self.share_txt_dir = share_txt_dir

    #计算基金总额=份额*净值 
    #share_txt_dir为/Users/szdbl/Documents/基金收益率监控/基金交易 目录下的txt文件地址
    def fund_worth(self,share_txt_dir):
        with open(self.share_txt_dir,'r+') as f:
            share=0
            #忽略标题，然后倒序排列
            lines = f.readlines()[1:][::-1]
            count=0
            for line in lines:
                line=list(line.strip('\n').split(','))
                #标记位：只取最新日期和相应的净值
                if count==0:
                    net_worth=float(line[2])
                    day=line[0]
                    count=count+1
                    #如果当前日期的记录的份额字段为空则往前取前一个日期的记录，直到非空的值
                if line[1]=='':
                    continue
                else:
                    share=float(line[1])
                    break
        return (datetime2.strptime(day,'%Y-%m-%d').date(),round(net_worth*share, 2))


    #计算xirr收益率，并将date,money,xirr写入xirr_txt_dir文件
    def fund_return(self,trad_txt_dir):
        fund_returns=[]
        fund_worths=0
    #计算xirr模块
        with open(self.trad_txt_dir,'r') as f:
    #忽略标题行
            lines = f.readlines()[1:]
            for line in lines:
                line=list(line.strip('\n').split(','))
    #将读取的数据转化成xirr函数要求的数据格式
                line[0]=datetime2.strptime(line[0],'%Y-%m-%d').date()
                line[1]=float(line[1])
                fund_returns.append(tuple(line))
    #将交易数据与最新的基金总额数据拼接起来
            fund_worths=self.fund_worth(self.share_txt_dir)
            fund_returns.append(fund_worths)
            return fund_worths,round(xirr.xirr(fund_returns),4)
        
        
      