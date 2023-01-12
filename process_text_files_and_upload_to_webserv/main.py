#! /usr/bin/env python3
import os
import requests

path =r"/data/feedback/"
url = "http://34.133.152.199/feedback/"
feedback_json = []
files = os.listdir(path)

for file in files:
    if file[0]!= '.':
        with open(path+file, 'r') as f:
            info = f.readlines()
            json_format = {}
            json_format["title"] = info[0].replace("\n","")
            json_format["name"] = info[1].replace("\n","")
            json_format["date"] = info[2].replace("\n","")
            json_format["feedback"] = info[3].replace("\n","")
            feedback_json.append(json_format)

for i in feedback_json:
    response = requests.post(url, json= i)
    print(response.raise_for_status())
