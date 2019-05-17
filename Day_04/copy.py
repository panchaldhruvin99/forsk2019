# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:13:10 2019

@author: Dhruvin Panchal
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

with open('words.txt','rt') as file :
   file_contents = file.read()
   with open('copy_words.txt','wt') as file1 :
       for content in file_contents:
           file1.write(content)
      

    