# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:58:37 2019

@author: Dhruvin Panchal
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
with open("absentee.txt",'a') as abs1:
    counter = 0
    while True:
       name = input("Enter the name of student ")
       if name ==" " or counter ==25:
           break
       else:
           abs1.write(name+'\n')
           counter +=1
with open ("absentee.txt",'rt') as abs1:
 print(abs1.readlines())           
    
 
      















       