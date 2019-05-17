#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:56:53 2018

@author: diva
"""

#Import data with numpy
#Define a function that takes an array
#For loop generating indicies
#If statement comparing difference to a maximum
#return position of max

import numpy as np
data = np.loadtxt(fname = 'Titration_color_data_simple.csv', \
                  delimiter = ',', \
                  skiprows = 1, \
                  usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))

def largest_change(row):
    maximum = 0
    for i in range(len(row)-1):
        difference = abs(row[i] - row[i+1])
        if difference > maximum:
            maximum = difference
            index = i+1
    return index


print(largest_change(data[1]))