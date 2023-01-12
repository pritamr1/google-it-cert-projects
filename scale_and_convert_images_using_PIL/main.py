#!/usr/bin/env python3
import os
from PIL import Image

img_files =next(os.walk(r"./images"))[2]

for img_file in img_files:
    if img_file[0] != '.':
        img = Image.open(r"./images/{}".format(img_file))
        img_rgb = img.convert('RGB')
        img_rgb.rotate(270).resize((128,128)).save(r"/opt/icons/{}{}".format(img_file,".jpeg"))

