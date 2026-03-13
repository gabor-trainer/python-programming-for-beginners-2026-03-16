import requests


def get_weather_by_city(city_name):
    """
    Fetches the current weather for a given city name using the Open-Meteo API.

    This is a two-step process:
    1. Geocoding: Convert city name to latitude and longitude.
    2. Weather: Fetch weather data using coordinates.
    """
    # 1. Geocoding API - Search for city coordinates
    geocoding_url = (
        f"https://geocoding-api.open-meteo.com/v1/search?"
        f"name={city_name}&count=1&language=en&format=json"
    )

    try:
        geo_response = requests.get(geocoding_url)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        # Check if the city exists in the database
        if not geo_data.get("results"):
            print(f"Error: Could not find location data for '{city_name}'.")
            return

        # Extract data from the first result
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        display_name = f"{location['name']}, {location.get('country', 'N/A')}"

        # 2. Weather API - Fetch current conditions
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&"
            f"current=temperature_2m,relative_humidity_2m,wind_speed_10m&"
            f"timezone=auto"
        )

        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current_weather = weather_data["current"]
        temperature = current_weather["temperature_2m"]
        humidity = current_weather["relative_humidity_2m"]
        wind_speed = current_weather["wind_speed_10m"]

        # Output the results
        print(f"\n--- Current Weather in {display_name} ---")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity:    {humidity}%")
        print(f"Wind Speed:  {wind_speed} km/h")

    except requests.exceptions.RequestException as error:
        print(f"Network error occurred: {error}")


if __name__ == "__main__":
    user_input = input(
        "Enter the city name (default: Győr): ").strip() or "Győr"

    get_weather_by_city(user_input)
