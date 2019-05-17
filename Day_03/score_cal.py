# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:32:00 2019

@author: Dhruvin Panchal
"""
"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

asg1 = float(input("Enter the marks of asg1"))
asg2 = float(input("Enter the marks of asg2"))
asg3 = float(input("Enter the marks of asg3"))

exam1 =float( input("enter the marks of exam1"))
exam2 =float( input("enter the marks of exam2"))

weighted_score = ( asg1 + asg2 + asg3) *0.1 + (exam1 + exam2 ) * 0.35
 
print(weighted_score)