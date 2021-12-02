#!/usr/bin/env python3
# libraries in use
from PIL import Image
import os

def convert_images(path):
    '''convert images from .tiff extension to .jpeg format.'''
    images = os.listdir(path)
    for image in images:
        # only convert images with .tiff extension
        if image.endswith('.tiff'):
            file = os.path.splitext(image)[0]
            save_to = "supplier-data/images/" + file + ".jpeg"
            try:
                # open current image, convert to jpeg, resize to 600 x 400 and save to give directory.
                jpeg_image = Image.open(path+image).convert('RGB').resize((600,400)).save(save_to,'JPEG')

            except IOError:
                print("Can't covert image {} to .jpeg extension".format(image))
        # skip any file without .tiff extension
        else:
            continue

    return 'Done converting images with .tiff to .jpeg extension!'

# directory where images stay.
dir_path = "supplier-data/images/"
# invoke function with directory as a path.
print(convert_images(path= dir_path))