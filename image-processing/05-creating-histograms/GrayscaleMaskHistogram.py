"""
 * Generate a grayscale histogram for an image.
 *
 * Usage: python GrayscaleMaskHistogram.py <filename>
"""
import sys
import numpy as np
import skimage.draw
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
img = skimage.io.imread(fname=sys.argv[1], as_gray=True)

# display the image
viewer = skimage.viewer.ImageViewer(img)
viewer.show()

# create mask here, using np.zeros() and skimage.draw.rectangle()

# mask the image and create the new histogram
histogram, bin_edges = np.histogram(img[mask], bins=256, range=(0.0, 1.0))

# configure and draw the histogram figure
plt.figure()

plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0.0, 1.0])
plt.plot(bin_edges[0:-1], histogram)

plt.show()