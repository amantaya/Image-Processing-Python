'''
 * Python script to demonstrate average blur.
 *
 * usage: python AverageBlur.py <filename> <kernel-size>
'''
import cv2
import sys

# get filename and kernel size from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read and display original image
img = cv2.imread(filename)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# apply average blur, creating a new image
blurred = cv2.blur(img, (k, k))

# display blurred image
cv2.namedWindow("blurred", cv2.WINDOW_NORMAL)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)
