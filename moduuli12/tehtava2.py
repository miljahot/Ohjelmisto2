import requests
import json
API_key = "d7926e34490880dea74f75cbbeedd0e5"

city_name = input("Syötä haettavan kaupungin nimi: ")
haku = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

try:
    vastaus = requests.get(haku)
    if vastaus.status_code ==200:
        json_vastaus = vastaus.json()

        for a in json_vastaus['weather']:
            print(f"Säätila: {a['description']}")
            print(f"Lämpötila: {json_vastaus['main']['temp']} °C")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")
