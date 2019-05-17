# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:26:31 2019

@author: Dhruvin Panchal
"""


"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""



"""
for item in list1:
    if item>0:
        return True

for item in list1:
    if (item==item[::-1]):
        return True
"""
list1 = [int(x) for x in  input("Enter the no.").split(" ")]

if all([item>0 for item in list1]) and any([str(item) == str(item)[::-1] for item in list1]):
    print ("True")
else:
    print ("False")
    
    









