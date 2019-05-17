# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:01:44 2019

@author: Dhruvin Panchal
"""

list2 = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowel = ['a','e','i','o','u','A','E','I','O','U']

output = []

for item in list2:
   new=''
   for char in item:
       if char not in vowel:
           new = new + char
        
   output.append(new)

print(output)       