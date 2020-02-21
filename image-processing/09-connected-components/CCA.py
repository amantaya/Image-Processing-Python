"""
 * Python script count objects in an image
 *
 * usage: python CCA.py <filename> <sigma> <threshold>
"""
import sys
import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.viewer
import skimage.measure
import skimage.color

# get filename, sigma, and threshold value from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])
t = float(sys.argv[3])

# read and display the original image
image = skimage.io.imread(fname=filename, as_gray=True)
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# blur and grayscale before thresholding
blur = skimage.filters.gaussian(image, sigma=sigma)

# perform inverse binary thresholding
mask = blur < t

# display the result
viewer = skimage.viewer.ImageViewer(mask)
viewer.show()

# Perform CCA on the mask
labeled_image, num = skimage.measure.label(mask, connectivity=2, return_num=True)

print("dtype:", labeled_image.dtype)
print("min:", np.min(labeled_image))
print("max:", np.max(labeled_image))

viewer = skimage.viewer.ImageViewer(labeled_image)
viewer.show()

# convert the label image to color image
colored_label_image = skimage.color.label2rgb(labeled_image, bg_label=0)

# show the created image in the viewer
viewer = skimage.viewer.ImageViewer(colored_label_image)
viewer.show()