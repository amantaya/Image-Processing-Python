#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:06:43 2017

Program to determine the connectedness of the nanoparticles in a
SEM image

usage: python NPConnect <filename> <d|nd>

@author: Mark M. Meysenburg
"""

import cv2, sys, numpy as np

# get filename, blur kernel size
filename = sys.argv[1]
wantDisplay = sys.argv[2]

# read image as grayscale
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# blur image 
blurImage = cv2.GaussianBlur(image, (3, 3), 0)

# create bianry image via Otsu's thresholding method
(t, binaryImage) = cv2.threshold(image, 0, 255, 
    cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# create binary image via edge detection
#binaryImage = cv2.Canny(image, 150, 210)

if wantDisplay == "d":
    cv2.namedWindow("binary", cv2.WINDOW_NORMAL)
    cv2.imshow("binary", binaryImage)
    cv2.waitKey(0)


# find contours in the image
(_, contours, _) = cv2.findContours(binaryImage, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# determine average length of the contours in the image
contourLengths = []
for c in contours:
    contourLengths.append(len(c))
averageContourLength = np.mean(contourLengths)

# output average contour length
print(filename, t, len(contours), averageContourLength, sep=",")