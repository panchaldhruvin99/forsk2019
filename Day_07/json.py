"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=dd87486981ae60a86cb5374fa15432e0"

url = url1 + url2 + url3
print (url)
response = requests.get(url)
response.content
print (type(response.content))

jsondata = response.json()
print (jsondata)

print(jsondata["coord"]["lon"])
print(jsondata["coord"]["lat"])

print(jsondata["weather"][0]["main"])

print(jsondata["wind"]["speed"])

print(jsondata["sys"]["sunrise"])
print(jsondata["sys"]["sunset"])