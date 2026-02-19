# weather_app.py

import requests
import config

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name, 
        "appid": api_key,
          "units": "metric"
          }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        print(f"\nWeather in {city_name.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather.capitalize()}")
    else:
        print("City not found. Please check the name.")

def main():
    print("=== Weather App ===")
    api_key = config.API_KEY  #THIS PULLS THE KEY FROM YOUR OTHER FILE
    city_name = input("Enter city name: ")
    get_weather(city_name, api_key)

if __name__ == "__main__":
    main()
