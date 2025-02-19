import json

class WeatherData:
    def __init__(self, json_file="global_weather.json"):
        self.json_file = json_file
        self.data = self.load_json()

    def load_json(self):
        """Load and validate JSON file."""
        try:
            with open(self.json_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    print("Error: JSON must be a list of cities.")
                    return []
                return data
        except FileNotFoundError:
            print(f"Error: File '{self.json_file}' not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")
            return []

    def get_weather_by_city(self, city_name):
        """Retrieve weather data for a specific city only from JSON."""
        for city in self.data:
            if city.get("name", "").lower() == city_name.lower():
                return {
                    "city": city.get("name", "N/A"),
                    "temperature": city.get("main", {}).get("temp", "N/A"),
                    "humidity": city.get("main", {}).get("humidity", "N/A"),
                    "weather": city.get("weather", [{}])[0].get("description", "N/A"),
                    "wind_speed": city.get("wind", {}).get("speed", "N/A"),
                    "pressure": city.get("main", {}).get("pressure", "N/A"),
                }
        return {"error": "Data not available"}

# Example usage
if __name__ == "__main__":
    weather_data = WeatherData("global_weather.json")
    
    # Example query
    city_name = input("Enter city name: ")
    result = weather_data.get_weather_by_city(city_name)
    
    print(result)  # Returns only JSON-based data or "Data not available"
