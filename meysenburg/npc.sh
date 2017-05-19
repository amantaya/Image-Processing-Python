#!/bin/bash
# Run the SEM nanoparticle connectedness program on every image

# then, execute the program on all the trail images
for f in ca35-*.tif
do
	python NPConnect.py $f nd
done
