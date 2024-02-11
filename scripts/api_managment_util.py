import requests
import json
import logging
from geopy.geocoders import Nominatim
from config.Credentials import API_KEY

def get_weather_data(lat: float, lon: float, api_key= API_KEY) -> dict:
    #Make an API call to OpenWeatherMap to retrieve the weather data for a specific location
    if api_key != "":
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
        response = requests.get(url)
        logging.info(f"API call to OpenWeatherMap: {response.status_code}")
        logging.info(f"API response: {response}")
        if response is not None:
            data = response.json()
            print(data) #TODO - Remove this print statement
            return data
        else:
            raise Exception(f"API call failed with status code {response.status_code}")
    else:
        raise Exception("API key is missing")
        

def get_device_location(location: str) -> tuple[str, float, float]:
    # Get the device's location using a geolocation service
    loc = Nominatim(user_agent="GetLoc")
    try:
        getLoc = loc.geocode(location)
        logging.info(f"API Location: {getLoc.address}")
        logging.info(f"API Latitude and Longitude: {getLoc.latitude} | {getLoc.longitude}")
        return (getLoc.address, getLoc.latitude, getLoc.longitude)
    except Exception as e:
        logging.error(f"Error: {e}")
        return (None, None) #TODO - Add a better error handling (Replace with raise Exception basen on return code)
    
    