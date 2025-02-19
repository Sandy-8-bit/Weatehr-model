import requests
import json
import time
from tqdm import tqdm

API_KEY = "0396fe1fc3e16a3fcca570677d66ae8d"

def get_weather_data(city_id):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_all_cities():
    with open("city.list.json", "r", encoding="utf-8") as file:
        cities = json.load(file)

    weather_data = []
    
    for city in tqdm(cities[:5000]):  # Limit to 5000 cities for testing
        data = get_weather_data(city["id"])
        if data:
            weather_data.append(data)
        time.sleep(1)  # API rate limit handling

    with open("global_weather.json", "w", encoding="utf-8") as file:
        json.dump(weather_data, file, indent=4)

    print("Weather data for all cities saved successfully!")

if __name__ == "__main__":
    fetch_all_cities()
