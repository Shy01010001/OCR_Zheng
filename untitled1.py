# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:16:10 2023

@author: hongyu
"""

import easyocr
import cv2
import time
import numpy as np
import math
import shutil
from glob import glob
import pyperclip
import os


    

# kernel = np.ones((3,3), np.uint8)
pre_pngs = glob('C:/Users/sunho/Downloads/*.png')
pre_o = len(pre_pngs)
while 1:
    l = []
    pngs = glob('C:/Users/sunho/Downloads/*.png')
    o = len(pngs)
    
    if o != pre_o:
        for png in pngs:
            if png not in pre_pngs:
                break
        imgName = png.split('\\')[-1]
        shutil.copy(png, 'D:/OCR_Zheng/' + imgName)
        
    
        image = cv2.imread(imgName)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = image.astype(np.float16)
        
        image = np.exp(3*image/255)
        
        image = image / np.max(image) * 255
        
        image = image.astype(np.uint8)
        
        # gray = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # gray = cv2.equalizeHist(gray)
        # gray = cv2.erode(gray, kernel)
        # image = cv2.dilate(image, kernel)
        cv2.imwrite('./gray.jpg',image)
        
        
        reader = easyocr.Reader(['ja','en']) 
        # 读取图像
        result = reader.readtext('gray.jpg')
        # print(result)
        # exit()
        text = ''
        for i in range(len(result)):
            post = [(result[i][0][0][0] + result[i][0][2][0]) / 2, (result[i][0][0][1] + result[i][0][2][1]) / 2]
            l.append([post, result[i][1]])
            text = text + result[i][1]
        print(l[0][1], end='')
        for i in range(1, len(result)):
            # print(abs(l[i][0][1] - l[i-1][0][1]))
            if abs(l[i][0][1] - l[i-1][0][1]) > 20:
                print()
                print(l[i][1],end = '')        
            else:
                if abs(l[i][0][0] - l[i-1][0][0]) > 30:
                    print(' '+l[i][1],end = '')
                else:
                    print(l[i][1], end = '')    
        pyperclip.copy(text)
        pre_pngs = pngs
        pre_o = o
           
