#!/usr/bin/env python3
# libraries in use
import os
import requests

def image_upload(path):
    ''' Upload images .jpeg extension to webserver '''
    ip_address = '34.66.62.242' # use IP address or domain name of a webserver.
    url = 'http://{}/upload/'.format(ip_address) # page or interface location
    images_files = os.listdir(path)
    # loop thru images.
    for image in images_files:
        # upload only image files with .jpeg extension in a given directory
        if image.endswith('.jpeg'):
            print('Image file: {}'.format(image))
            with open(path+image,'rb') as to_upload:
                try:
                    response = requests.post(url, files={'file': to_upload})
                    print('File {} is successfully uploaded with success code of: {}'.format(to_upload, response.status_code))
                except:
                    print('File {} failed to be uploaded due to error code of: {}'.format(to_upload, response.status_code))
        # skip images without .jpeg extensions given directory
        else:
            continue

    return 'Done uploading images with .jpeg extensions to: {}'.format(url)

# directory where images stay.
dir_path = "supplier-data/images/"
# invoke function with directory as a path.
print(image_upload(path= dir_path))
