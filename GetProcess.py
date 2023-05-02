# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:25:41 2023

@author: hongyu
"""

import cv2
import pytesseract
from pytesseract import Output
from FigSeg import Set
import re

# def remove_unwanted_characters(text):
#     # 定义一个正则表达式，匹配日文字符、英文字母、标点符号和数字
#     # \u3040-\u309F: 平假名
#     # \u30A0-\u30FF: 片假名
#     # \u4E00-\u9FFF: 常用汉字
#     # a-zA-Z: 英文字母
#     # \u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E: ASCII标点符号
#     # 0-9: 数字
#     pattern = r"[^\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFFa-zA-Z\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E0-9]"
    
#     # 使用re.sub函数替换不匹配的部分为空字符串
#     result = re.sub(pattern, "", text)
    
#     return result

# # 图像文件名
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sunho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# flag = 0
# # Set()
# # while 1:
# #     try:
# #         image_name = f'00{flag}.jpg'
        
# #         # 读取图像
# #         image = cv2.imread(image_name)
        
# #         # 使用pytesseract进行OCR识别
# #         config = '-l jpn'  # 如果图像中包含日语文本，请指定日语参数
# #         data = pytesseract.image_to_data(image, output_type=Output.DICT, config=config)
        
# #         # 提取表格中的文本
# #         rows = []
# #         current_row = []
# #         current_block_num = data['block_num'][0]
# #         for i in range(len(data['text'])):
# #             if data['block_num'][i] != current_block_num:
# #                 if current_row:
# #                     rows.append(' '.join(current_row))
# #                 current_row = []
# #                 current_block_num = data['block_num'][i]
# #             if data['text'][i].strip():
# #                 current_row.append(data['text'][i])
# #         if current_row:
# #             rows.append(' '.join(current_row))
        
# #         # 将文本行合并为一个字符串
        
# #         text = '\n'.join(rows)
# #         text = remove_unwanted_characters(text)
# #         print(text)
# #         print()
# #         flag+=1
# #     except:
# #         break

# img = cv2.imread('000.jpg')
# df = pytesseract.image_to_data(img, lang='jpn', output_type = 'data.frame')

# df = df[['text', 'left', 'top', 'width', 'height']]
# # df = df[df['conf'] > -1]
# df = df.sort_values(['top', 'left']).reset_index(drop=True)
# grouped = df.groupby('top')
# result = ''
# for _, group in grouped:
#     result += ' '.join(group['text'].tolist()) + '\n'
# print(result)
    