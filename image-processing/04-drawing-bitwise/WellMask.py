import numpy as np
import skimage
from skimage.viewer import ImageViewer
import sys

image = skimage.io.imread(fname="wellplate.tif", plugin = 'pil')
viewer = ImageViewer(image)
viewer.show()

mask = np.ones(shape=image.shape[0:2], dtype="bool")

with open('centers.txt') as center_file:
    for line in center_file:
        tokens = line.split()
        x = int(tokens[0])
        y = int(tokens[1])

        rr, cc = skimage.draw.circle(y, x, radius = 16)
        mask[rr, cc] = False

# apply mask
image[mask] = 0

viewer = ImageViewer(image)
viewer.show()

skimage.io.imsave('masked.jpg', arr = image)