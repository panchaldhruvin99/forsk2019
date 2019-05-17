# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:38:43 2019

@author: Dhruvin Panchal
"""

list4 = input("Enter the numbers").split(" ")
print(list4)
for x in list4:
    if(int(x)<10):
        a= "true"
        break
    elif(x==x[::-1]):
        a= "true"
        break
    else:
        a="false"
        
print(a)        
        
        
      
        