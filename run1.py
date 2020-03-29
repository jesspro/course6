#! /usr/bin/env python3

import os
import requests
import json

text_list = []
keys = ["name", "weight", "description", "image_name"]

directory = os.path.normpath(os.path.join(os.getcwd(), "supplier-data", "descriptions"))
url = "http://35.238.32.211/fruits/"

for file in os.listdir(directory):
    if file.endswith(".txt"):
        text_list.append(file)

for ff in text_list:
    entry_dict = {}
    filename = os.path.splitext(ff)[0]
    with open(os.path.join(directory,ff)) as fp:
        for x in range(4):
            line = fp.readline()
            if x == 1:
                w = float("".join(ele for ele in line if ele.isdigit() or ele == "."))
                entry_dict[keys[x]] = w
            if x == 3:
                entry_dict[keys[x]] = (filename + ".jpeg")
            else:
                entry_dict[keys[x]] = line.strip()
    entry_json = json.dumps(entry_dict)
    response = requests.post(url, json=entry_json)
    print(response.status_code)
    print(entry_dict)


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
