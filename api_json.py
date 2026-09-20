# Weather
import requests
from geopy.geocoders import Nominatim
import csv

geolocator = Nominatim(user_agent="learn_python")
location = geolocator.geocode("Bardejov")

url = f"https://archive-api.open-meteo.com/v1/archive?latitude={location.latitude}&longitude={location.longitude}&start_date=2026-09-20&end_date=2026-09-20&hourly=temperature_2m"
response = requests.get(url)
data = response.json()

# Structure data
structure_data = []

for i in range(len(data["hourly"]["time"])):
    structure_data.append({
        "location": location.raw["name"],
        "time": data["hourly"]["time"][i],
        "temperature": data["hourly"]["temperature_2m"][i]
    })

with open('temperature.csv', 'w', newline='') as csvfile:
    fieldnames = ['location', 'time', 'temperature']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(structure_data)