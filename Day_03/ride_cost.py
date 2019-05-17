# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:22:28 2019

@author: Dhruvin Panchal
"""
"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
"""   

kilom = input("Enter the kilometer you travel in fro")
avg = input("enter the avg of your car")
cost = input("cost of the fuel ")

total_ltr = int(kilom)/int(avg)

daily_cost = int(total_ltr)*int(cost)

print(daily_cost)

