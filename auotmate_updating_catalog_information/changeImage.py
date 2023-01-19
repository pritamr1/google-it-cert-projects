#!/usr/bin/env python3
import os
from PIL import Image
path = r"/home/student-02-26b21f26a289/supplier-data/images/"
img_files =os.listdir(r"/home/student-02-26b21f26a289/supplier-data/images/")

for img_file in img_files:
    if img_file[-5:] == '.tiff':
        img = Image.open(r"/home/student-02-26b21f26a289/supplier-data/images/{}".format(img_file))
        img_rgb = img.convert('RGB')
        img_file = img_file.replace(".tiff",".jpeg")
        img_rgb.resize((600,400)).save(r"/home/student-02-26b21f26a289/supplier-data/images/{}".format(img_file))