"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""

import sqlite3
from pandas import DataFrame

conn = sqlite3.connect("db_university.db")

c=conn.cursor()

c.execute ( 
          """CREATE TABLE student(
            student_name TEXT,
            student_age INTEGER,
            student_roll_no INTEGER,
            student_branch TEXT)"""
         )
          
c.execute("DROP TABLE IF EXISTS student;")
         
c.execute("INSERT INTO student VALUES ('Dhruvin',21,053,'CSE')")
c.execute("INSERT INTO student VALUES ('honey',22,054,'CSE')")
c.execute("INSERT INTO student VALUES ('Dhruv',21,055,'CSE')")
c.execute("INSERT INTO student VALUES ('manas',22,056,'CSE')")
c.execute("INSERT INTO student VALUES ('aayush',21,057,'CSE')")
         

c.execute("SELECT * FROM student")

print ( c.fetchall() )     


c.execute("SELECT * FROM student")
df = DataFrame(c.fetchall()) 
df.columns = [" student_name ",
            "student_age ",
            "student_roll_no ",
            "student_branch "]    

conn.commit()
conn.close()