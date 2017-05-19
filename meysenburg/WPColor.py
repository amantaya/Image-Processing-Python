#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:18:02 2017

@author: diva
"""

import cv2, sys, numpy as np

# get filename
filename = sys.argv[1]

# read original image
image = cv2.imread(filename)

# create a mask for the well plate
xInit = 210
yInit = 240

mask = np.zeros((1982, 1351, 3), dtype = "uint8")

for x in range(xInit, 1200, 140):
    for y in range(yInit, 1850, 140):
        cv2.circle(mask, (x, y), 45, (255, 255, 255), -1)
        
# apply mask to the image
selectedImage = cv2.bitwise_and(image, mask)

cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.namedWindow("selected image", cv2.WINDOW_NORMAL)
cv2.imshow("selected image", selectedImage)
cv2.waitKey(0)