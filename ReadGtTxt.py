# -*- coding: utf-8 -*-
"""
Created on Mon May  1 08:49:01 2023

@author: youjingyi
"""
a = []
for line in open('./output/gt.txt', encoding = 'shift-jis'):
    print(line)
    a.append(line)
# 创建一个用于保存新闻文本文件的目录
