#!/usr/bin/env python3
import requests
import os

path=r"/home/student-02-26b21f26a289/supplier-data/images/"
url = "http://34.132.9.202/upload/"
imgs = os.listdir(path)

for img in imgs:
    if img[-4:] == "jpeg" and img[0] != '.': 
        with open(path+img, 'rb') as opened:
            r = requests.post(url,files = {'file': opened})
