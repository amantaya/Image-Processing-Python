#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:53:51 2018

@author: diva
"""

# Create a variable with the file name
filename = 'PracticeOutputFile.txt'

# Open the file in "write" mode
outfile = open(filename, 'w')

#now I can write to this file
outfile.write("This is first line of text.\n")
outfile.write("This is the second line of text.")


# Close the file!
outfile.close()



