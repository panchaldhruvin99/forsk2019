# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:21:39 2019

@author: Dhruvin Panchal
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
def counter(item):
    list1 = ['13','14','17','18','19']
    a = len(item)
    sum = 0 
    for i in range(0,a):
         if item[i] not in list1:
             sum = sum + int(item[i])
         else:
             pass
    return sum    
            
            
            
            
            
keys = input("Enter the keys").split(" ")

age = input("Enter the ages ").split(" ")

dict1 = dict(zip(keys ,age ))
print(dict1)

list2= list(dict1.values())
print(counter(list2))



























