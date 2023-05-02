# -*- coding: utf-8 -*-
"""
Created on Tue May  2 08:11:53 2023

@author: youjingyi
"""

from trdg.generators import(
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)

imgNum = 0
with open('./output/gt.txt', 'a', encoding = 'shift-jis') as f:
    for line in open('./result.py', encoding = 'shift-jis'):
        imgNum = imgNum.zfill(8)
        t = f'{imgNum}.png    ' + line
        f.write(t, encoding = 'shift-jis')
        imgNum += 1
        generator = GeneratorFromStrings(
            [line],
            random_blur = False
        )
        for img, lbl in generator:
            print(type(img))
        break