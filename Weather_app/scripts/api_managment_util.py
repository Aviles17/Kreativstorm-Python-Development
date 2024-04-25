import requests
import logging
import os
from geopy.geocoders import Nominatim
from geopy.point import Point
from config.Credentials import API_KEY
from src.weather import weather

def get_weather_data(lat: float, lon: float, api_key= API_KEY) -> dict:
    #Make an API call to OpenWeatherMap to retrieve the weather data for a specific location
    if api_key != "":
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
        response = requests.get(url)
        logging.info(f"API call to OpenWeatherMap: {response.status_code}")
        logging.info(f"API response: {response}")
        if response is not None:
            data = response.json()
            return data
        else:
            raise RuntimeError(f"API call failed with status code {response.status_code}")
    else:
        raise FileNotFoundError("API key is missing")
        

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
        return (None, None)
    
def get_adress_latlong(lat: float, lon: float) -> str:
    #Get the address of the location using the latitude and longitude
    loc = Nominatim(user_agent="GetLoc")
    try:
        getLoc = loc.reverse(Point(lat, lon))
        logging.info(f"API Location: {getLoc.address}")
        return getLoc.address
    except Exception as e:
        logging.error(f"Error: {e}")
        return None 
    
def decompose_json_info(data: dict) -> weather:
    #Decompose the JSON data returned by the API call
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    description = data['weather'][0]['description']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    country = data['sys']['country']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    timezone = data['timezone']
    imageicon = data['weather'][0]['icon']
    return weather(lat, lon, description, temp_min, temp_max, feels_like, humidity, country, sunrise, sunset, timezone, imageicon)

def get_icon(icon: str) -> str:
    #Get the weather icon
    if os.path.isfile(f"resources/{icon}@2x.png"):
        return f"resources/{icon}@2x.png"
    elif os.path.isfile(f"resources/0{icon[1]}@2x.png"):
        return f"resources/0{icon[1]}@2x.png"
    elif os.path.isfile(f"resources/1{icon[1]}@2x.png"):
        return f"resources/1{icon[1]}@2x.png"
    elif os.path.isfile(f"resources/5{icon[1]}@2x.png"):
        return f"resources/5{icon[1]}@2x.png"
    else:
        logging.error(f"Icon {icon} not found")
        raise FileNotFoundError(f"Icon {icon} not found")