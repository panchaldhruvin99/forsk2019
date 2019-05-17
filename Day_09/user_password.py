# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:15:37 2019

@author: Dhruvin Panchal
"""



client = pymongo.MongoClient("mongodb://Dhruvin:<porsche%400001>@cluster0-shard-00-00-geijb.mongodb.net:27017,cluster0-shard-00-01-geijb.mongodb.net:27017,cluster0-shard-00-02-geijb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.test
