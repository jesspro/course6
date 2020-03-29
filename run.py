#! /usr/bin/env python3

import os
import requests

# you will have to process the .txt files (named 001.txt, 002.txt)
# in the supplier-data/descriptions/ directory
# and save them in a data structure so you can upload via JSON

#note all files are written in the following format with 
#each piece of info on its own line
#name
#weight in lbs
#description

#the data model in the Django application fruit has the following fields:
#name
#weight
#description
#image_name

#sample json
#{"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}

#when you process the weight info from the txt file, you need
#to convert it to an integer.

#the image_name field will allow the system to find the image associated
#with the fruit, don't forget to add all fields including image_name

#the final json object should be similar to 
#{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}

#iterate over all the fruits and use post methon from Python requests library to upload all the data to the URL http://[linux-instance-external-IP]/fruits
