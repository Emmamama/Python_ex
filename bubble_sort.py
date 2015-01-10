# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 23:28:03 2015

@author: apple
"""
def bubble_sort(lst):
    top = len(lst) - 1
    is_exchanged = True
    
    while is_exchanged:
        is_exchanged = False
        for i in range(top):
            if lst[i] > lst [i + 1]:
                is_exchanged = True 
                swap(lst, i, i+1)
        top -= 1
        
lst = [1,12, 10, 8, 33]

bubble_sort(lst)

print lst