import requests

def fetch_weather_data(city_name):
    api_key = "your_openweather_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    response = requests.get(base_url)
    data = response.json()
    return data