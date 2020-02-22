"""
 * Program to practice with skimage drawing methods.
"""
import random
import numpy as np
import skimage
from skimage.viewer import ImageViewer

# create the black canvas
image = np.zeros(shape=(600, 800, 3), dtype="uint8")
viewer = ImageViewer(image)
viewer.show()

# mask = np.ones(shape=image.shape[0:2], dtype="bool")

# WRITE YOUR CODE TO DRAW ON THE IMAGE HERE
rr1, cc1 = skimage.draw.circle(300, 400, radius=100)
image[rr1, cc1] = [128, 25, 128]

# display the results
# Display constructed mask
viewer = ImageViewer(image)
viewer.show()