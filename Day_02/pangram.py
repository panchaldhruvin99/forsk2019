# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:25:34 2019

@author: Dhruvin Panchal
"""

str1 = input("Enter the String")
count=0
str2 = "abcdefghijklmnopqrstuvwxyz"

for i in range(0,26):
    if str2[i] in str1:
        count=count+1
        pass
        
    else:
         print("String is not pangram")
         break
    if count==26: 
         print("String is pangram")
         
        
        
