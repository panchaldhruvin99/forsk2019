# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:32:12 2019

@author: Dhruvin Panchal
"""

list1 =input("Enter the no.").split(" ")
print(list1)

def ADD(list1):
    add = 0
    for i in list1:
        add = add + int(i)
    return add    

print(ADD(list1))

def multiply(list1):
    mul = 1
    for i in list1:
        mul = mul* int(i)
    return mul

print (multiply(list1))    
        
def largest(list1):
    a = len(list1)
    print (a)
    for i in range(0,a):
        if list1[i]>list1[i+1]:
            value=list1[i]
    return value
print(largest(list1))        
