#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:09:53 2020
基金收益率监控程序-文件路径生成模块
@author: szdbl
"""
import os


class Fund_File_Generator(object):
    def __init__(self,trad_file_dir): 
        self.trad_file_dir = trad_file_dir  
    #读取file_dir目录下所有txt文件名
    def file_name(self):   
        L=[]   
        for root, dirs, files in os.walk(self.trad_file_dir):  
            for file in files:  
                if os.path.splitext(file)[1] == '.txt':  
                    file_name = file[0:-4]  #去掉.txt
                    L.append(file_name)  
        return L 