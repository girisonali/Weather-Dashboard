import requests

print("Weather Dashboard")
api_key = "0e7f2c72af6f4052f88792fedd3beb8e"
base_url = "https://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter city name (or type 'exit' to quit): ").strip()
    
    if city.lower() == "exit":
        print("Exiting the Weather Dashboard.")
        break

    if not city:
        print("Please enter a valid city name.")
        continue

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feel_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"].get("speed", "N/A")

        print(f"\nWeather in {city}, {country}: ")
        print("-------------------------------")
        print(f"Temperature: {temp}°C (feels like: {feel_like}°C)")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s \n")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e} - Please check the city name or your internet connection.")
    except KeyError:
        print("Error: Unable to fetch all weather data. Try again.")
