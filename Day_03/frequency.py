# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:54:10 2019

@author: Dhruvin Panchal
"""


"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
str1 = input("Enter The string" )

freq = {}

for char in str1:
    if char not in freq:
        freq[char]=1
    else:
        freq[char]=freq[char]+1
        
print(freq)        























