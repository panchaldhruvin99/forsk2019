# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:20:11 2019

@author: Dhruvin Panchal
"""




list2 = input("Enter the days").split(" ")

Total_Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']



for day in Total_Days:
    if day not in list2:
     list2.append(day)
        
print(tuple(list2))        