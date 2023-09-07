#!/usr/bin/env python3
import os
import requests

json_data = []

path = r"/home/student-02-26b21f26a289/supplier-data/images/"
files = os.listdir(path)
for file in files:
    if file[-3:] == "txt":
        with open(path + file, 'r') as f:
            info = f.readlines()
            info = [x.replace("\n","") for x in info]
            json_format = {}
            json_format["name"] = info[0]
            json_format["weight"] = int(info[1].replace(" lbs",""))
            json_format["description"] = info[2]
            json_format["image_name"] = file[:-3] + "jpeg"
            json_data.append(json_format)

for x in json_data:
    request = requests.post("http://34.132.9.202/fruits/", json = x)
    print(request.status_code)