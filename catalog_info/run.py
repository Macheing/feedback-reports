#! /usr/bin/env python3
import os
import requests

def image_descriptions(path):
    ip_address = '34.66.62.242' # IP address of webserver.
    url = 'http://{}/fruits/'.format(ip_address) # page location
    description_files = os.listdir(path) # list of image descrition files.
    for file in description_files:
        # grep any file with .txt extension.
        if file.endswith('.txt'):
            print('File name: {}'.format(file))
            with open (path+file, 'r') as txt_file:
                data = txt_file.read().split('\n') # split by new line.
                # change file extension from .txt to .jpeg
                image_name= os.path.splitext(file)[0]+'.jpeg'
                # json or dictionary format
                to_dict = {'name': data[0], 'weight': int(data[1].strip('lbs')), 
                            'description': data[2] + '\n\n\n', 'image_name': image_name }
                try:
                    # post given json data to database thru api
                    response = requests.post(url, json=to_dict)
                    response.raise_for_status()
                    req_url = response.request.url
                    print('File {} is successfully uploaded to {} with success code of: {}'.format(file,req_url,response.status_code))
                except:
                    print('File {} failed to be uploaded due to error code of: {}'.format(file, response.status_code))
        # skip any file without .txt extension.
        else:
            continue 

    return "Done uploding images' descriptions to {}".format(url)

# directory where images desciptions stay.
dir_path = "supplier-data/descriptions/"
# invoke function with directory as a path.
print(image_descriptions(path= dir_path))