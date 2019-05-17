#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:25:52 2018

@author: diva
"""

tot = 0
for num in range(2,11,2):
    tot = tot + num
print(tot)

for num in range(3):
    print(num+1)
    
the = range(1,4)
for num in the:
    print(num)
    
word = 'Newton'
newWord = ''
for letter in word:
    print(letter,  newWord)
    newWord = letter + newWord
print(newWord)