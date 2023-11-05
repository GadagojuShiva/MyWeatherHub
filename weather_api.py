# Import necessary libraries
import requests
import json
import time

# Define your API key for accessing weather data
API_KEY = "9b8447ce275e4f45b49133216230511"

# Function to get weather data for a given city
def get_weather_data(city):
    # Construct the URL with the API key and the city
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"
    # Send an HTTP GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)
        return data
    else:
        # Raise an exception if the API request failed
        raise Exception("Failed to retrieve weather data for the city.")

# Function to print weather information
def print_weather_data(data):
    # Extract location and current weather data
    location = data["location"]
    current = data["current"]
    
    # Print weather information
    print("Location: " + location["name"])
    print("Temperature: " + str(current["temp_c"]) + "°C / " + str(current["temp_f"]) + "°F")
    print("Humidity: " + str(current["humidity"]) + "%")
    print("Wind Speed: " + str(current["wind_mph"]) + " mph / " + str(current["wind_kph"]) + " km/h")
    print("Wind Direction: " + current["wind_dir"])

# Input favorite cities from the user
print("Please enter your favorite cities separated by spaces:")
favourite_cities = input().split()
print("Your favorite cities:", favourite_cities)

# Data validation for the city name
data_validation = False
while data_validation == False:
    city = input("Please enter the name of a city: ")
    try:
        if city.isalpha():
            data_validation = True
        else:
            print("City names should only contain alphabetic characters.")
    except:
        print("Invalid city name format.")

# Retrieve and display weather data for the selected city
if data_validation == True:
    weather_data = get_weather_data(city)
    print("Weather information for", city + ":")
    print_weather_data(weather_data)
