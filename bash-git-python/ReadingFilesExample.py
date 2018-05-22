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
data = inputfile.readlines()

for line in data[1:]:
    sline = line.strip()
    sline = sline.split(',')

    colonyCount = int(sline[4])
    
    if colonyCount > 30:
        print(sline)
   
"""    
    if 'control' in line:
        print(line)
"""
        
#Close the file when we're done!
inputfile.close()

