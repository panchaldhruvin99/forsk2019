"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi"""

from bs4 import BeautifulSoup 
import requests

import sqlite3

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text  
#print(source)

soup = BeautifulSoup(source,"lxml")

#print (soup.prettify())

right_table=soup.find('table', class_="table")

print (right_table)



A=[]
B=[]
C=[]
D=[]

for team in right_table.findAll("tr"):
    online=team.findAll("td")
    if len(online) == 5:
        A.append(online[1].text.strip())
        B.append(online[2].text.strip())
        C.append(online[3].text.strip())
        D.append(online[4].text.strip())

for item range(0,15):
    
    c.execute("INSERT INTO student VALUES ('')")


