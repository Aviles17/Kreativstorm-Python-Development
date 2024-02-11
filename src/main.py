''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''
    

import tkinter as tk
from PIL import Image #Pillow to display the weather icons (Images)
import datetime as dt
import logging
from scripts.api_managment_util import get_weather_data
from scripts.api_managment_util import get_device_location

def open_input_latlong_window():
    #Create a new window to input the location
    input_window = tk.Toplevel(main_window)
    input_window.title("Location Input")
    #Create labels and entry fields for the latitude and longitude
    lbl_lat = tk.Label(input_window, text="Latitude:")
    lbl_lat.pack(padx=10, pady=10)
    entry_lat = tk.Entry(input_window)
    entry_lat.pack(padx=10, pady=10)
    lbl_lon = tk.Label(input_window, text="Longitude:")
    lbl_lon.pack(padx=10, pady=10)
    entry_lon = tk.Entry(input_window)
    entry_lon.pack(padx=10, pady=10)
    #Create a submit button to fetch the weather data
    btn_submit = tk.Button(input_window, text="Submit", command=lambda: get_weather_data(float(entry_lat.get()), float(entry_lon.get())))
    btn_submit.pack(padx=10, pady=10)
    
def open_input_location_window():
    #Create a new window to input the location
    input_window = tk.Toplevel(main_window)
    input_window.title("Location Input")
    #Create labels and entry fields for the location
    lbl_location = tk.Label(input_window, text="Location:")
    lbl_location.pack(padx=10, pady=10)
    entry_location = tk.Entry(input_window)
    entry_location.pack(padx=10, pady=10)
    #Create a submit button to fetch the weather data
    btn_submit = tk.Button(input_window, text="Submit", command=lambda: result_window_location(entry_location.get()))
    btn_submit.pack(padx=10, pady=10)
    
def result_window_latlong(lat: float, long:float):
    pass

def result_window_location(location: str):
    adress, lat, long = get_device_location(location)
    data = get_weather_data(lat, long)
    #Create a new window to display the weather data
    result_window = tk.Toplevel(main_window)
    result_window.title("Weather Data")
    #Create labels to display the weather data
    lbl_location = tk.Label(result_window, text=f"Location: {adress}")
    lbl_location.pack(padx=10, pady=10)
    lbl_temp = tk.Label(result_window, text=f"{data}")
    lbl_temp.pack()

if __name__ == "__main__":
    #Configure the logging module
    logging.basicConfig(filename="weather_app.log", level=logging.DEBUG)
    #Create a GUI for the weather app
    main_window = tk.Tk()
    main_window.title("Kreativstorm Weather App") #Create a title for the window
    btn_fetch = tk.Button(main_window, text="Input Location Name", command=open_input_location_window)
    btn_fetch.pack(padx=10, pady=100)

    btn_input = tk.Button(main_window, text="Input Lat/Long Information ", command=open_input_latlong_window)
    btn_input.pack(padx=100, pady=100)    
    main_window.mainloop()
    