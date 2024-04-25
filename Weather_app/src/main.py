import tkinter as tk
from PIL import Image, ImageTk #Pillow to display the weather icons (Images)
import datetime as dt
import logging
from scripts.api_managment_util import get_weather_data
from scripts.api_managment_util import get_device_location
from scripts.api_managment_util import decompose_json_info
from scripts.api_managment_util import get_icon
from scripts.api_managment_util import get_adress_latlong

def open_input_latlong_window():
    #Create a new window to input the location
    input_window = tk.Toplevel(main_window)
    input_window.title("Location Input")
    input_window.geometry("400x200")
    input_window['bg'] = '#9494b8'
    #Create labels and entry fields for the latitude and longitude
    lbl_location = tk.Label(input_window, text="Please enter the name of the location:",  bg='#9494b8', fg='black', font=("Helvetica",  16, "bold"))
    lbl_location.grid(row=0, column=0, columnspan=2, sticky='nsew')
    lbl_lat = tk.Label(input_window, text="Latitude:", bg='#9494b8')
    lbl_lat.grid(row=1, column=0)
    entry_lat = tk.Entry(input_window, bg='#9494b8')
    entry_lat.grid(row=1, column=1, sticky='ew')
    
    lbl_lon = tk.Label(input_window, text="Longitude:", bg='#9494b8')
    lbl_lon.grid(row=2, column=0)
    entry_lon = tk.Entry(input_window, bg='#9494b8')
    entry_lon.grid(row=2, column=1, sticky='ew')
    def submit(lat: float, long: float):
        input_window.destroy()
        result_window_latlong(lat, long)
    #Create a submit button to fetch the weather data
    btn_submit = tk.Button(input_window, text="Submit", command=lambda: submit(float(entry_lat.get()), float(entry_lon.get())), bg='#9494b8')
    btn_submit.grid(row=3, column=0, columnspan=2)
    input_window.columnconfigure(0, weight=1)
    input_window.columnconfigure(1, weight=1)
    input_window.rowconfigure(0, weight=1)
    input_window.rowconfigure(1, weight=1)
    input_window.rowconfigure(2, weight=1)
    
def open_input_location_window():
    #Create a new window to input the location
    input_window = tk.Toplevel(main_window)
    input_window.title("Location Input")
    input_window['bg'] = '#9494b8'
    input_window.geometry("400x200")
    #Create labels and entry fields for the location
    lbl_location = tk.Label(input_window, text="Please enter the name of the location:",  bg='#9494b8', fg='black', font=("Helvetica",  16, "bold"))
    lbl_location.pack(padx=10, pady=10)
    entry_location = tk.Entry(input_window, bg='#9494b8')
    entry_location.pack(padx=10, pady=10)
    def submit(location: str):
        input_window.destroy()
        result_window_location(location)
    #Create a submit button to fetch the weather data
    btn_submit = tk.Button(input_window, text="Submit", command=lambda: submit(entry_location.get()), bg='#9494b8')
    btn_submit.pack(padx=10, pady=10)
    
def result_window_latlong(lat: float, long:float):
    adress = get_adress_latlong(lat, long)
    data = get_weather_data(lat, long)
    w_object = decompose_json_info(data)
    #Create a new window to display the weather data
    result_window = tk.Toplevel(main_window)
    result_window.geometry("700x400")
    #result_window.resizable(False, False)
    result_window['bg'] = '#9494b8'
    result_window.title("Weather Data")
    
    #Create labels to display the weather data
    lbl_location = tk.Label(result_window, text=f"{adress}", bg='#9494b8', fg='black', font=("Helvetica",  16, "bold"), wraplength=500)
    lbl_location.grid(row=0, column=0, columnspan=2, sticky='nsew')
    
    #First row (Latitude and Longitude)
    lbl_lat = tk.Label(result_window, text=f"Latitude: {lat}", bg='#9494b8', fg='black')
    lbl_long = tk.Label(result_window, text=f"Longitude: {long}", bg='#9494b8', fg='black')
    lbl_lat.grid(row=1, column=0)
    lbl_long.grid(row=1, column=1)
    
    #Second row (Temperature and sensation)
    lbl_temp_max = tk.Label(result_window, text=f"Max Temperature: {w_object.temp_max}°C", bg='#9494b8', fg='black') 
    lbl_temp_min = tk.Label(result_window, text=f"Min Temperature: {w_object.temp_min}°C", bg='#9494b8', fg='black')
    lbl_temp_max.grid(row=2, column=0)
    lbl_temp_min.grid(row=2, column=1)
    
    #Third row (Weather description and humidity)
    lbl_sensation = tk.Label(result_window, text=f"Feels like: {w_object.feels_like}°C", bg='#9494b8', fg='black')
    lbl_hum = tk.Label(result_window, text=f"Humidity: {w_object.humidity}%", bg='#9494b8', fg='black')
    lbl_sensation.grid(row=3, column=0)
    lbl_hum.grid(row=3, column=1)
    
    #Fourth row (Description)
    lbl_desc = tk.Label(result_window, text=f"{w_object.description}".upper(),bg='#9494b8', fg='black', font=("Helvetica",  16, "bold"))
    lbl_desc.grid(row=4, column=0, columnspan=2) 
    
    #Fifth row (Incon Image)
    img = Image.open(get_icon(w_object.imagecode))
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(result_window, image=photo, bg='#9494b8')
    image_label.image = photo
    image_label.grid(row=5, column=0, columnspan=2) 
    
    #Column - row configure
    result_window.columnconfigure(0, weight=1)
    result_window.columnconfigure(1, weight=1)
    result_window.rowconfigure(0, weight=1)
    result_window.rowconfigure(1, weight=1)
    result_window.rowconfigure(2, weight=1)
    result_window.rowconfigure(3, weight=1)
    result_window.rowconfigure(4, weight=1)
    result_window.rowconfigure(5, weight=1)
    

def result_window_location(location: str):
    adress, lat, long = get_device_location(location)
    data = get_weather_data(lat, long)
    w_object = decompose_json_info(data)
    #Create a new window to display the weather data
    result_window = tk.Toplevel(main_window)
    result_window.geometry("700x400")
    #result_window.resizable(False, False)
    result_window['bg'] = '#9494b8'
    result_window.title("Weather Data")
    
    #Create labels to display the weather data
    lbl_location = tk.Label(result_window, text=f"{adress}", bg='#9494b8', fg='black', font=("Helvetica",  16, "bold"),  wraplength=500)
    lbl_location.grid(row=0, column=0, columnspan=2, sticky='nsew')
    
    #First row (Latitude and Longitude)
    lbl_lat = tk.Label(result_window, text=f"Latitude: {lat}", bg='#9494b8', fg='black')
    lbl_long = tk.Label(result_window, text=f"Longitude: {long}", bg='#9494b8', fg='black')
    lbl_lat.grid(row=1, column=0)
    lbl_long.grid(row=1, column=1)
    
    #Second row (Temperature and sensation)
    lbl_temp_max = tk.Label(result_window, text=f"Max Temperature: {w_object.temp_max}°C", bg='#9494b8', fg='black') 
    lbl_temp_min = tk.Label(result_window, text=f"Min Temperature: {w_object.temp_min}°C", bg='#9494b8', fg='black')
    lbl_temp_max.grid(row=2, column=0)
    lbl_temp_min.grid(row=2, column=1)
    
    #Third row (Weather description and humidity)
    lbl_sensation = tk.Label(result_window, text=f"Feels like: {w_object.feels_like}°C", bg='#9494b8', fg='black')
    lbl_hum = tk.Label(result_window, text=f"Humidity: {w_object.humidity}%", bg='#9494b8', fg='black')
    lbl_sensation.grid(row=3, column=0)
    lbl_hum.grid(row=3, column=1)
    
    #Fourth row (Description)
    lbl_desc = tk.Label(result_window, text=f"{w_object.description}".upper(),bg='#9494b8', fg='black', font=("Helvetica",  16, "bold"))
    lbl_desc.grid(row=4, column=0, columnspan=2) 
    
    #Fifth row (Incon Image)
    img = Image.open(get_icon(w_object.imagecode))
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(result_window, image=photo, bg='#9494b8')
    image_label.image = photo
    image_label.grid(row=5, column=0, columnspan=2) 
    
    #Column - row configure
    result_window.columnconfigure(0, weight=1)
    result_window.columnconfigure(1, weight=1)
    result_window.rowconfigure(0, weight=1)
    result_window.rowconfigure(1, weight=1)
    result_window.rowconfigure(2, weight=1)
    result_window.rowconfigure(3, weight=1)
    result_window.rowconfigure(4, weight=1)
    result_window.rowconfigure(5, weight=1)

if __name__ == "__main__":
    #Configure the logging module
    logging.basicConfig(filename="weather_app.log", level=logging.DEBUG)
    #Create a GUI for the weather app
    main_window = tk.Tk()
    main_window.title("Kreativstorm Weather App") #Create a title for the window
    main_window.geometry("700x400")
    main_window['bg'] = '#9494b8'
    lbl_title = tk.Label(main_window, text="Weather App", bg='#9494b8', fg='black', font=("Helvetica",  16, "bold"))
    lbl_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
    #Add Image and time
    img = Image.open("resources\\03@2x.png")
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(main_window, image=photo, bg='#9494b8')
    image_label.grid(row=1, column=0, columnspan=2) 
    #Show current time and date
    now = dt.datetime.now()
    lbl_time = tk.Label(main_window, text=f"Current Time: {now.strftime('%Y-%m-%d %H:%M:%S')}", bg='#9494b8', fg='black')
    lbl_time.grid(row=2, column=0, columnspan=2)    
    #Create buttons to fetch the weather data
    btn_fetch = tk.Button(main_window, text="Input Location", command=open_input_location_window,bg='#9494b8')
    btn_fetch.grid(row=3, column=0, sticky='ew')

    btn_input = tk.Button(main_window, text="Input Lat-Long", command=open_input_latlong_window, bg='#9494b8')
    btn_input.grid(row=3, column=1, sticky='ew')
    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=1)
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=1)
    main_window.rowconfigure(2, weight=1)
    main_window.rowconfigure(3, weight=1)
    main_window.mainloop()
    