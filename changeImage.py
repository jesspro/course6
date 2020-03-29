#!/usr/bin/env python3

from PIL import Image

import glob,os

size = 600, 400

for infile in glob.glob("/supplier-data/images/*.tiff"):
    im = Image.open(infile).convert("RGB")
    im.resize((size)).save("/supplicer-data/images/" + infile + ".JPEG", "JPEG")



#you will be using the PIL library to update all images within
#~/supplier-data/images directory
#size: change resol. to 600x400
#format: change from .tiff to .jpeg

#after processing the images, save them in ~/supplier-data/images
#with JPEG extension


