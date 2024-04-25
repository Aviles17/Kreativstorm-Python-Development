# Weather_app

Weather app shows the current weather conditions and forecast for a specific location. Python project that uses OpenWeatherMap and Geocoder's API. Basic GUI build in tkinter and Pillow libraries

## Objectives

- Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.
- Use the json library to parse the JSON data returned by the API call.
- Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.
- Use the Pillow library to display the weather icons.
- Use the datetime library to display the current time and date

## Instalation

To setup the project and flawlessly execute the app you should follow these steps

```bash
  cd ./Weather_App
  pip install -e .
  pip install -r ./requirements.txt
```
It's also necesary that the file located in config/Credentials_template.py is cloned or renamed as Credentials.py, add your api key following the template to use OpenWeatherMap API, and save the file.

## Author

- [Santiago Avilés Tibocha](https://github.com/Aviles17)
