# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:11:59 2019

@author: Dhruvin Panchal
""""""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
"""

car = input("Enter the killometer")

fuel =input("enter the fuel in liters")

avg = int(car)/int(fuel)
print(avg)
