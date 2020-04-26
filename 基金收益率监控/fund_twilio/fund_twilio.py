#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:14:07 2020
基金收益率监控程序-短信通知模块
@author: szdbl
"""

from twilio.rest import Client
accountSID='你的accountSID'
authToken='你的authToken'
myNumber='+86手机号'
twilioNumber='你的twilioNumber'



class Fund_Return_Twilio(object):
    def __init__(self,message): 
        self.message = message
        
    def fund_twilio(self):
        twilioCli = Client(accountSID,authToken)
        twilioCli.messages.create(
                body=self.message,
                from_=twilioNumber,
                to=myNumber)
        

