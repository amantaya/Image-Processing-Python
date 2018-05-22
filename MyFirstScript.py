# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Create variables
AreaInPixels = 6929  # This is hte area in pixels
mm2PerPixel = 0.0277 # This is the conversion factor

#Calculate the converted area
AreaInMM = AreaInPixels * mm2PerPixel

#Print the final result
print("The area in mm2 is: ", AreaInMM)

