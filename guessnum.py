# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 22:20:49 2015

@author: apple
"""

import random
num = random.randint(10,99)

guess_num = 0
i = 0

while guess_num != num:
    guess_num = int(input("Enter your guess number:"))
    if guess_num > num:
        print "You should enter a90 smaller number!"
        print num
        
    elif guess_num < num:
        print "You should enter a larger number!"        
    i = i + 1
    28
if guess_num == num:
    print "That is it! Bravo!"
else:
    print "Take another around. Good luck!"
    
print i


    



