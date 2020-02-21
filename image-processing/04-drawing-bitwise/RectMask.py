"""
 * Python program to use skimage drawing tools to create a mask.
 *
"""
import skimage
from skimage.viewer import ImageViewer
import numpy as np

# Load and display the original image
image = skimage.io.imread("maize-roots.tif")
viewer = ImageViewer(image)
viewer.show()

# Create the basic mask
mask = np.zeros(shape=image.shape[0:2], dtype="bool")

# Draw filled rectangle on the mask image
rr, cc = skimage.draw.rectangle(start=(357, 44), end=(740, 720))
mask[rr, cc] = True

# Display constructed mask
viewer = ImageViewer(mask)
viewer.show()