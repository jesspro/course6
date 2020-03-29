#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

directory = os.path.normpath(os.path.join(os.getcwd(), "supplier-data", "images"))

for infile in os.listdir(directory):
    if infile.endswith(".jpeg"):
        with open(os.path.join(directory,infile), "rb") as opened:
            r = requests.post(url, files={"file": opened})
