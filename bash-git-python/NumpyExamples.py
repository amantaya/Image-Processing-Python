#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:55:06 2018

@author: diva
"""

import numpy as np

data = np.loadtxt(fname = 'Plates_output_simple.csv', delimiter=',', skiprows = 1, usecols=(1,2,3,4,5,6))

print(data.shape)

print(data[2,0]) #first number is row, second is column

print(data[2, :]) #Will return all of row two
print(data[:, 2]) #will return all of column two

print(data[1:3, 5:11])

print(np.max(data))
print(np.min(data))
print(np.mean(data))
print(np.std(data))

# Apply standard dev to each row

print(np.std(data[0, ]))

print(np.std(data, axis=0)) #applies to each column
print(np.mean(data, axis = 1)) #applies to each row






















