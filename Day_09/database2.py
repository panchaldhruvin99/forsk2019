"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.

"""

import pymongo

client = pymongo.MongoClient("mongodb://Dhruvin:porsche%400001@cluster0-shard-00-00-geijb.mongodb.net:27017,cluster0-shard-00-01-geijb.mongodb.net:27017,cluster0-shard-00-02-geijb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.dhruvin
def add_panchal( student_name,
            student_age ,
            student_roll_no ,
            student_branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.panchal.insert_one(
            {
            "NAME" : student_name,
            "AGE" : student_age,
            "Roll_No" : student_roll_no,
            "Branch" : student_branch
            })
    return "Employee added successfully"


def fetch_all_panchal():
    user = mydb.panchal.find()
    for i in user:
        print (i)




add_panchal('Dhruvin',21,'053','CSE')
add_panchal('bahavya',22,'054','CSE')
add_panchal('honey',23,'055','CSE')
add_panchal('Dhruv',21,'056','CSE')


fetch_all_panchal()
