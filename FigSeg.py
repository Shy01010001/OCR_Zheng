# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:40:04 2023

@author: hongyu
"""

import cv2
import pytesseract
from pytesseract import Output
import numpy as np

# 加载图像
def Set():
    image = cv2.imread('000.jpg', cv2.IMREAD_GRAYSCALE)
    
    # 使用Tesseract进行OCR，并获取文本的边界框信息
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    
    # 初始化一个列表来存储段落的边界框
    paragraphs = []
    current_paragraph = []
    
    # 设置垂直距离阈值，用于判断文本块之间的距离是否足够大以划分为不同段落
    vertical_threshold = 50
    
    # 遍历每个文本块，根据文本块的垂直位置来确定段落的边界
    for i in range(len(d['text'])):
        if d['text'][i].strip():
            x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
            if current_paragraph and abs(y - current_paragraph[-1][1]) > max(vertical_threshold, h):
                paragraphs.append(current_paragraph)
                current_paragraph = []
            current_paragraph.append((x, y, w, h))
    
    if current_paragraph:
        paragraphs.append(current_paragraph)
    
    # 根据段落的边界框裁剪图像，并保存为单独的图像文件
    for i, paragraph in enumerate(paragraphs):
        x_min = min([x for x, _, _, _ in paragraph])
        y_min = min([y for _, y, _, _ in paragraph])
        x_max = max([x + w for x, _, w, _ in paragraph])
        y_max = max([y + h for _, y, _, h in paragraph])
        paragraph_image = image[y_min:y_max, x_min:x_max]
        cv2.imwrite(f'{i+1:03d}.jpg', paragraph_image)
    
    print(f'Total {len(paragraphs)} paragraphs saved.')
