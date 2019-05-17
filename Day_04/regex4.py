# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:35:31 2019

@author: Dhruvin Panchal
"""

"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""
import re

emails = input("Enter the email").split(",")
list1 = []
 
for item in emails:
    list2 = re.findall(r"^\w+@+[a-z]+\.[a-z]{3}",item)
    list1.append(list2)
list3 = sorted(list1) 
for i in list3:
    print(i)
    