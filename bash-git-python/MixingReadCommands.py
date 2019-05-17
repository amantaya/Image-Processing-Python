#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:05:43 2018

@author: diva
"""

# Create a variable to hold the file name 
filename = 'Plates_output_simple.csv'

# Open the file
inputfile = open(filename, 'r')

data1 = inputfile.read()
data2 = inputfile.readline()


print(data1)
print(data2)


# Always close the file!
inputfile.close()