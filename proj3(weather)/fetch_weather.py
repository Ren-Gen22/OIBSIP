import os
import json
import requests
from dotenv import load_dotenv

location="Chennai" #input("Enter location:")
load_dotenv()
api=os.getenv("API_KEY")
url=f"http://api.weatherapi.com/v1/current.json?key={api}&q={location}"
response=requests.get(url)
if response.status_code == 200:
    data_dict = response.json()
else:
    print(f"Error: {response.status_code}")

def get_conditon():
    return data_dict["current"]["condition"]["text"]
def get_icon():
    return data_dict["current"]["condition"]["icon"]
def get_temperature(unit):
    if unit=="c":
        return data_dict["current"]["temp_c"],data_dict["current"]["feelslike_c"]
    elif unit=="f":
        return data_dict["current"]["temp_f"],data_dict["current"]["feelslike_f"]
print(get_temperature("c"))
