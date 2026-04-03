import requests

api_key = "69c9b8a79b6c161c1809eb22b008ec41"
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"🌡️ Temperature: {temp}°C")
    print(f"🌤️ Condition: {weather}")
else:
    print("❌ City not found!")