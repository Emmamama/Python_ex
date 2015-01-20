# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 18:50:27 2015

@author: apple
"""

s = 'sinsiso'

lst = [0] * 26

for i in s:
    lst[ord(i) - 97] += 1

print lst
