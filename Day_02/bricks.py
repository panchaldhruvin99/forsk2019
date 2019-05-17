# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:11:41 2019

@author: Dhruvin Panchal
"""

AA = int(input("Enter the no. of bricks of 5 inch."))

BB = int(input("Enter the no. of bricks of 1 inch."))

Target = int(input("Enter the length "))

Total = int(BB)*1+int(AA)*5

if(Total >= Target):
       print("True")
       
else:
      print("false")
     