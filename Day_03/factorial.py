# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:53:32 2019

@author: Dhruvin Panchal
"""

"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""
import math
fact1 =int( input("enter the no."))

a = math.factorial(fact1)
print(a)