# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:53:37 2019

@author: Dhruvin Panchal
"""
"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

with open ("romeo.txt") as fp1:
    dict1 = {}
    
    for item in fp1.readlines():
        list1 = item.split(" ")
        for word in list1:
            if word not in dict1:
                dict1[word]=1
            else:
                dict1[word] = dict1[word]+1
                
    print(dict1)        