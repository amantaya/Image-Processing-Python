#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:44:17 2018

@author: diva
"""

#Create a variable for the file name
filename = 'Plates_output_simple.csv'

##Open the file
infile = open(filename, 'r') 

lines = infile.readlines() #We will process the lines of the file later
	
#close the input file
infile.close()

#Create the file we will write to
filename = 'ControlPlatesData.txt' 
outfile = open(filename, 'w')

outfile.write(lines[0]) #This will write the header line of the file 

for line in lines[1:]: #skip the first line, which is the headersl
    sline = line.strip()
    sline = sline.split(',')  # separates line into a list of items.  ',' tells it to split the lines at the commas
    
    if "control" in sline:
        outfile.write(','.join(sline) + '\n') #The variable line is already formatted correctly!

outfile.close() #Close the file when we’re done!

