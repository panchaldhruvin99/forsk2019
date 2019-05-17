# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:28:32 2019

@author: Dhruvin Panchal
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
import pymongo

client = pymongo.MongoClient("mongodb://Dhruvin:porsche%400001@cluster0-shard-00-00-geijb.mongodb.net:27017,cluster0-shard-00-01-geijb.mongodb.net:27017,cluster0-shard-00-02-geijb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.dhruvin

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://bidplus.gem.gov.in/bidlists"
"""//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a
//*[@id="pagi_content"]/div[2]/div[1]/p[1]/a
//*[@id="pagi_content"]/div[1]/div[2]/p[1]/strong
//*[@id="pagi_content"]/div[2]/div[2]/p[1]/strong
//*[@id="pagi_content"]/div[2]/div[2]/p[2]/strong
//*[@id="pagi_content"]/div[3]/div[2]/p[2]/strong
//*[@id="pagi_content"]/div[1]/div[3]/p[1]/strong
//*[@id="pagi_content"]/div[2]/div[3]/p[1]/strong
"""

browser = webdriver.Chrome("E:/Forsk Technologies/chromedriver.exe")
browser.get(url)


sleep(2)

A=[]
B=[]
C=[]
D=[]

for i in range(1,11):
    A.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[1]/p[1]/a").text)    
    B.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[1]/strong").text)
    C.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[2]/strong").text)
    D.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[3]/p[1]/strong").text)


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)

for item in range(0,10):
    
       mydb.panchal.insert_one(
            {
            "NAME" : A[item],
            "AGE" : B[item],
            "Roll_No" : C[item],
            "Branch" : D[item]
            })
def fetch_all_panchal():
    user = mydb.panchal.find()
    for i in user:
        print (i)
        
fetch_all_panchal()

sleep(3)


browser.quit()

