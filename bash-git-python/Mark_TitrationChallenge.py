#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:58:41 2018

@author: diva
"""
import numpy as np

'''
 * Function to find the frame where largest change happens in a row
 * of color channel values. 
 *
 * @param row 1D array of color channel values, each in [0, 255]
 * @return frame where largest change occurs
'''
def largestChange(row):
    # compute absolute values of differences between
    # successive elements of the array
    diffs = np.abs(np.diff(row))
    # return index of largest difference, plus 1
    return np.argmax(diffs) + 1
  
'''
 * Main program begins here
'''          
data = np.loadtxt(fname = 'Titration_color_data_simple.csv', 
                  delimiter =',', skiprows = 1, 
                  usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))

print('Row 0 largest change in frame', largestChange(data[0,:]))
print('Row 1 largest change in frame', largestChange(data[1,:]))
print('Row 2 largest change in frame', largestChange(data[2,:]))

# testing data from Web lesson
intensities = [140, 142, 139, 128, 129, 126]

print('Test data largest change in frame', largestChange(intensities))
