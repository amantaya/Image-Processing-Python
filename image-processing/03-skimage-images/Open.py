'''
 * Python program to open, display, and save an image.
 *
'''
import skimage.io

# read image 
image = skimage.io.imread(fname="chair.jpg")

import skimage.viewer

# display image
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# save a new version in .tif format
skimage.io.imsave(fname="chair.tif", arr=image)