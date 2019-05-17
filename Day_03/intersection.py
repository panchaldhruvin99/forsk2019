# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:52:56 2019

@author: Dhruvin Panchal
"""

a = { 1,2,2,3,3,4,5 }
print(type (a) ) 
print (a) 

##########

list1 = [1,3,4,5,6,7]
list2 = [2,4,5,6,7,8]

s1 = set(list1)
s2 = set(list2)

s3 = s1.intersection(s2)
print(s3)