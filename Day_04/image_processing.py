# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:04:29 2019

@author: Dhruvin Panchal
"""


"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""
from PIL import Image

img = Image.open("small_sample1.jpg")
img= img.transpose(Image.ROTATE_90)
img.thumbnail((150, 100))
img = img.crop(box=(0, 0, 160, 240))
img = img.convert("LA")
img.show()







