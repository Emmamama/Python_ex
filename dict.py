# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 18:52:45 2015

@author: apple
"""

s = 'agasiulja'

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print d