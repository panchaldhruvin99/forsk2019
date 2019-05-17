# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:44:04 2019

@author: Dhruvin Panchal
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""


def reverse1(str1):
    s1=" "

    for i in str1:
       s1 = i + s1
   
    return s1


str1 = input("Enter the String")
reverse1(str1)


