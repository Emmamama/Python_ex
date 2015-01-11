# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 20:50:01 2015

@author: apple
"""

words = ['abc', 'defgh', 'kjs', 'wosuud']

words.sort(key = lambda x: len(x), reverse = True)

print words
