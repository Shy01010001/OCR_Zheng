# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:49:49 2023

@author: youjingyi
"""

from trdg.generators import(
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)
	# The generators use the same arguments as the CLI, only as parametersgenerator=GeneratorFromStrings(
imgNum = 0
with open('./output/gt.txt', 'a', encoding = 'shift-jis') as f:
    for line in open('./data/GT/result.txt', encoding = 'shift-jis'):
        imgN = str(imgNum).zfill(8)
        t = f'images/{imgN}.png    ' + line
        generator = GeneratorFromStrings(
        [line],
        # blur=2,
        random_blur=False,
        language = 'ja'
        )
        try:
            
            for img, lbl in generator:
            # print(generator[0])
                img.save(f'./output/images/{imgN}.png')
                break
            f.write(t)
            imgNum += 1
        except:
            print(line,' cannot generate image!')
                
