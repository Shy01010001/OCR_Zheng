# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:13:46 2023

@author: youjingyi
"""
import unicodedata

def is_jan(char):
    c = unicodedata.category(char)
    if c == 'Lo' or c == 'Po' or c == 'Ps' or char == '\n':
        return True
    return False

# decoded_string = byte_string.decode('utf-8')1
with open('./TextGet&Clear/karineno_yume.txt', encoding = 'shift-jis') as f:
    t = f.read()

Proc_t = ''
for ch in t:
    if is_jan(ch):
        Proc_t += ch

with open('./data/result.txt', 'a', encoding = 'shift-jis') as result:
    result.write(Proc_t)
