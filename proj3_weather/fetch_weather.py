import os
import json
import requests
from dotenv import load_dotenv

class Weatherify:
    data_dict = {}

    def __init__(self, location):
        self.location = location
        load_dotenv()
        api = os.getenv("API_KEY")
        url = f"http://api.weatherapi.com/v1/current.json?key={api}&q={location}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data_dict = response.json()  
        else:
            print(f"Error: {response.status_code}")


    def get_condition(self):
        return self.data_dict["current"]["condition"]["text"]

    def get_icon(self):
        return self.data_dict["current"]["condition"]["icon"]

    def get_temperature(self, unit):
        if unit == 0:
            return self.data_dict["current"]["temp_c"], self.data_dict["current"]["feelslike_c"]
        elif unit == 1:
            return self.data_dict["current"]["temp_f"], self.data_dict["current"]["feelslike_f"]


