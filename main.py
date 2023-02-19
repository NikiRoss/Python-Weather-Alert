import os
import weather
import message

api_key = os.environ.get('WEATHER_APP_API_KEY')
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
lat = input("Type in the latitude for your area ")
lon = input("Please enter the longitude for your area ")

forecast = weather.Weather(api_key, lat, lon)

message = message.Message(account_sid, auth_token)

message.create_message(forecast.get_forecast())

print(account_sid)
