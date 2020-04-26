#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:14:45 2020
xirr算法实现
@author: szdbl
"""
#import datetime
from scipy import optimize
 
# 函数
def xnpv(rate, cashflows):
    return sum([cf/(1+rate)**((t-cashflows[0][0]).days/365.0) for (t,cf) in cashflows])
 
def xirr(cashflows, guess=0.1):
    try:
        return optimize.newton(lambda r: xnpv(r,cashflows),guess)
    except:
        print('Calc Wrong')
 
# 
## 测试
#data = [(datetime.date(2006, 1, 24), -39967), (datetime.date(2008, 2, 6), -19866), 
#        (datetime.date(2010, 10, 18), 245706), (datetime.date(2013, 9, 14), 52142)]
#xirr(data)



