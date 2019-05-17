#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:07:30 2018

@author: diva
"""

areas = [6829, 8527, 2214, 17743]
print(areas)

samples = ['Plate15', 'Plate20', 'Plate293']
print('The samples are:', samples)

#Add an item to the list samples
samples.append('Plate17')
print('Samples after:', samples)

# We can also make empty lists
plateCounts = []
print("This list is empty ", plateCounts)

# Add values to my empty list
plateCounts.append(43)
plateCounts.append(296)

print("PlateCounts after: ", plateCounts)

#Delete items from a list
samples.remove('Plate20')
print('Samples after removing: ', samples)

print(samples[2])

print(samples[-1])
print(samples[-2])

#We can replace items in a list
print("The areas are: ", areas)
areas[1] = 7527
print("Now areas are: ", areas)

print(areas[1:4])

print(areas[:3])
print(areas[1:])


print(len(areas))




















