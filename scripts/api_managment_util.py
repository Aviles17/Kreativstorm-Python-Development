import requests
import json
import logging
from config.Credentials import API_KEY

def get_weather_data(lat: float, lon: float, api_key= API_KEY) -> dict:
    #Make an API call to OpenWeatherMap to retrieve the weather data for a specific location
    if api_key != "":
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={api_key}"
        response = requests.get(url)
        logging.info(f"API call to OpenWeatherMap: {response.status_code}")
        logging.info(f"API response: {response}")
        if response is not None:
            data = response.json()
            return data
        else:
            raise Exception(f"API call failed with status code {response.status_code}")