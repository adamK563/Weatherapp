import requests
import sys
sys.path.append('../')
sys.path.append('../')
sys.path.append('../')
sys.path.append('../')
from backend.core.config import settings

# API key
api_key = settings.API_WEATHER_KEY

# API endpoint
url = settings.WEATHER_API_URL

# list of cities
cities = settings.CITIES

def connect_weather():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def calculate_weather():
    # create empty list to store city latitudes and longitudes
    city_locations = []
    temprtures = []
    # loop through each city
    for city in cities:
        # complete URL with API key and city
        complete_url = url + "appid=" + api_key + "&q=" + city

        # GET request to API endpoint
        response = requests.get(complete_url)

        # extract data from response
        data = response.json()

        # convert temperature from Kelvin to Celsius
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = round(temperature_kelvin - 273.15, 2)

        latitude = data["coord"]["lat"]
        longitude = data["coord"]["lon"]
        city_locations.append((latitude, longitude))
        temprtures.append(temperature_celsius)
    
    return city_locations, temprtures

'''
Client-Specific Implementation
The code block below is dedicated to the client-side of the application.
'''

def get_map_size(city_locations):
    # create map centered at the average latitude and longitude of the cities
    mean_latitude = sum(x[0] for x in city_locations) / len(city_locations)
    mean_longitude = sum(x[1] for x in city_locations) / len(city_locations)
    return [mean_latitude, mean_longitude]

def get_location_and_weather():
    try:
       weather_data = connect_weather()
    except weather_data.error as error:
        raise ConnectionError("Failed to connect to server: {0}".format(error))
    return calculate_weather()
    