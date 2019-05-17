# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:30:51 2019

@author: Dhruvin Panchal
"""

str1 = input("Enter the string 1")

str2 = input("Enter the string 2")

a=len(str1)
b=len(str2)
count=0

if a==b:
    for i in str1:
        if i in str2:
            count = count+1
            continue
        else:
            print("Not annagram")
            
    if count ==a:
            print("Annagram")
    else:
            print("not")
else:
  print("not annagram")            