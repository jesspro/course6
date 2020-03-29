#!/usr/bin/env python3

from PIL import Image

import os

directory = os.path.normpath(os.path.join(os.getcwd(), "supplier-data", "images"))
print(directory)

size = (600, 400)

for infile in os.listdir(directory):
    if infile.endswith(".tiff"):
        filename = os.path.splitext(infile)[0]
        new_filename = filename + ".jpeg"
        im = Image.open(os.path.join(directory,infile)).convert("RGB")
        im.resize(size).save(os.path.join(directory,new_filename), "JPEG")



#you will be using the PIL library to update all images within
#~/supplier-data/images directory
#size: change resol. to 600x400
#format: change from .tiff to .jpeg

#after processing the images, save them in ~/supplier-data/images
#with JPEG extension
