#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:06:47 2018

@author: diva
"""

print('PlateCountsExample')

plateCounts = [43, 207, 6, 1247]
for number in plateCounts:
    if number > 30 and number < 300:
        print(number, 'the plate is countable')
    else:
        print('the plate is out of range')
        
bmps = []
pngs = []
jpgs = []

images = ['image1.png', 'image2.jpg', 'image3.bmp', 'image4.jpg', 'image5.png']

for filename in images:
    if filename[-3:] == 'png':
        pngs.append(filename)
    elif filename[-3:] == 'jpg':
        jpgs.append(filename)
    elif filename[-3:] == 'bmp':
        bmps.append(filename)
    else:
        print(filename, 'is not there')
        
print(pngs)
print(jpgs)
print(bmps)
    