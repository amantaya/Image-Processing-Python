#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:04:30 2018

@author: diva
"""

filename = "NumbersOutput.txt"

outfile = open(filename, 'w')

numbers = range(1,11)

for number in numbers:
    outfile.write(str(number) + '\n')
    
outfile.close()