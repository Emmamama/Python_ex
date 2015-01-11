# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 20:44:08 2015

@author: apple
"""

words = ['abc', 'defgh', 'kjs', 'wosuud']
#装饰（新成一个新的列表）
lst = []

for word in words:
    lst.append((len(word),word))
    
lst.sort(reverse = True)

res = []

for length, word in lst:
    res.append(word)
    
print res