
"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests

d1 = int(input("enter the usd value"))
url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=4b37ace06d0c80536078"

response = requests.get(url)



jsondata = response.json()
print(jsondata)

print(d1*jsondata["USD_INR"])
