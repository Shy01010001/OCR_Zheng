# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:11:37 2023

@author: hongyu
"""

import cv2
import pytesseract
import matplotlib.pyplot as plt

# 加载图像
image = cv2.imread('000.jpg')

# 图像预处理
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# plt.imshow(gray,cmap = 'gray')
# plt.show
# cv2.waitKey()
# OCR
text = pytesseract.image_to_string(image, lang='jpn')

# 位置识别
# positions = pytesseract.image_to_boxes(image)

# # 将识别出的文字输出到控制台
# for position in positions.splitlines():
#     position = position.split(' ')
#     x, y, w, h = int(position[1]), int(position[2]), int(position[3]), int(position[4])
#     print(position[0], (x, image.shape[0] - y))

