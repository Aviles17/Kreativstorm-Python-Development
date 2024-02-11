class weather:
    #Define object constructor
    def __init__(self, lat: float, lon: float, description: str, temp_min: float, temp_max:float, feels_like: float, humidity: float, country: str, sunrise: int, sunset: int, timezone: int):
        self.lat = lat
        self.lon = lon
        self.description = description
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.feels_like = feels_like
        self.humidity = humidity
        self.country = country
        self.sunrise = sunrise
        self.sunset = sunset
        self.timezone = timezone
    
    #Define object string representation
    def __str__(self):
        return f"Weather(lat={self.lat}, lon={self.lon}, description={self.description}, temp_min={self.temp_min}, temp_max={self.temp_max}, feels_like={self.feels_like}, humidity={self.humidity}, country={self.country}, sunrise={self.sunrise}, sunset={self.sunset}, timezone={self.timezone})"
    