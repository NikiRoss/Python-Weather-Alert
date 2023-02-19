import requests
import json


class Weather():
    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

        
    def get_forecast(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            location = data["name"]
            weather = data["weather"][0]["main"]
            return f"Weather = {location}, {weather}"
        else:
            return f"There was an error retrieving your forecase, please ensure you have provided accurate information"
        


