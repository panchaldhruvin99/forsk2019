# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:31:02 2019

@author: Dhruvin Panchal
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need1 by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
"""
with open('zoo.csv','rt') as zoo1:
    zoo_content = zoo1.readlines()
    for row in zoo_content:
        print(row)
        
"""        
import csv
with open("zoo.csv") as zoo1:
    csv_reader = csv.reader(zoo1, delimiter=",")
    
    elephant=0
    elephant_list=[]
    tiger=0
    tiger_list=[]
    zebra = 0
    zebra_list= []
    lion = 0
    lion_list = []
    for row in csv_reader:
        if row[0]=="elephant":
            elephant = elephant+int(row[2])
            elephant_list.append(row[1]) 
        elif row[0]=="tiger":
            tiger = tiger+int(row[2])
            tiger_list.append(row[1])
        elif row[0]=="zebra":
            zebra = zebra+int(row[2])
            zebra_list.append(row[1])
        elif row[0]=="lion":
            lion = lion+int(row[2])
            lion_list.append(row[1])
            
    print("Elephant in grp and total water",elephant,elephant_list)         
    print("tiger in grp and total water",tiger,tiger_list)         
    print("zebra in grp and total water",zebra,zebra_list)         
    print("lion in grp and total water",lion,lion_list)         
    print("Water by all animals",elephant+tiger+zebra+lion)
















