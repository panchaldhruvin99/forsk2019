# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:36:05 2019

@author: Dhruvin Panchal
"""

name = input("Enter the name of item").split(",")

values = input("Enter the values").split(",")

dict1 = dict(zip(name , values))
print(dict1)



