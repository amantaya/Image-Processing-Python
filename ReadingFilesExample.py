#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:54:48 2018

@author: diva
"""

# Create a variable to hold the file name 
filename = 'Plates_output_simple.csv'

# Open the file
inputfile = open(filename, 'r')

# Read the file
data = inputfile.read()

print(data)


#Close the file when we're done!
inputfile.close()

