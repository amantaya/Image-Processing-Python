#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:58:04 2018

@author: diva
"""

def challenge(filename, row):

    data = np.loadtxt(fname = filename,
                  delimiter =',', skiprows = 1,
                  usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
    next_num = 1
    high_diff = 0
    index = 0
    
    for num in data[row-1,:14]:

        if abs(num - data[row-1,next_num]) > high_diff:
            index = next_num 
            high_diff = abs(num - data[row-1,next_num])
        next_num += 1
    return("the greatest difference was ",high_diff
           ," at the location ",index )
                
        
    
print(challenge('Titration_color_data_simple.csv',1))