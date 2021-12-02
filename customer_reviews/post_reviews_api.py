#! /usr/bin/env python3
import os
import requests

data_path = '/customer_reviews/' # data path
Ip_address = '34.134.44.83'  # webserver ip address
feedback_files = os.listdir(data_path) # list of directory files

# go through each file in directory.
for file in feedback_files:
    print('File name: {}'.format(file)) # print file name
    with open(data_path+file,'r') as feed_data: # open file
        data = feed_data.read().split('\n') 
        to_dict = {'title':data[0],'name':data[1],'date':data[2],'feedback':data[3]}
        print(to_dict)
        try:
            response = requests.post('http://{}/feedback/'.format(Ip_address),json=to_dict)
            print('Data posted:',response.status_code)
        except:
            print('Error! {}'.format(response.status_code))

