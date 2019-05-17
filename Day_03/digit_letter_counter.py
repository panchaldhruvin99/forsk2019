# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:16:54 2019

@author: Dhruvin Panchal
"""

str2= input("ENTER the string")

str3='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

str4= '1234567890'

alpha=0
digit=0

for i in str2:
    if i in str3:
        alpha = alpha+1
    else:
        digit=digit+1
        
print(alpha)
print(digit)        