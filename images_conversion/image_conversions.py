
#!/usr/bin/env python3
from PIL import Image
import os

old_path = os.path.expanduser('~')+'/images/' # path of images you want to convert
new_path = '/opt/icons/' # path you want to store newly convertes images

for image_file in os.listdir(old_path): # iterate through images directory.
    try:
        # open image files
        image = Image.open(old_path + image_file)
        # rotate image 90 degree clockwise, change size to 128 x 128, 
        # convert image to .jpeg and save it new directory.
        image.rotate(-90).resize((128,128)).convert('RGB').save(new_path+image_file+'.jpeg')
    except:
        print('Error occurred!:', image_file , 'can not be converted to .jpeg file.')
    finally:
        image.close()
