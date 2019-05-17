# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:12:59 2019

@author: Dhruvin Panchal
""""""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

file = input("Ener the file name ")
with open(file,'rt')as a:
    dhr = a.readlines()
    print(dhr)
    print(dhr[-1])

