import requests

def fetch_weather(location):
    api_key = "e34e4d4fed74f52fae4f57b2b39f890a"  # Add your OpenWeatherMap API key here
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Construct the URL with location and API key
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return f"The weather in {location} is {weather_description} with a temperature of {temperature}°C."
    else:
        return f"Sorry, I couldn't fetch the weather for {location}."

# Example usage
# print(fetch_weather("New York"))
