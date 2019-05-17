# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:43:58 2019

@author: Dhruvin Panchal
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
with open("words.txt") as fp1:
    
    nub_char = 0
    nub_wrd = 0
    nub_line = 0
    nub_unq = 0
    
    for item in fp1.readlines():
        nub_line = nub_line + 1
        nub_wrd = nub_wrd + len(item.split(" "))
        nub_unq = nub_unq + len(set(item.split(" ")))
        
        for i in item :
            nub_char = nub_char+1
            
print(nub_char)
print(nub_line)
print(nub_wrd)
print(nub_unq)            
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    