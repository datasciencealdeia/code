import requests

cidade = "Curitiba"
<<<<<<< HEAD

geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
   "name": cidade,
   "count": 1
}
=======
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
    "name": cidade,
    "count": 1
}

>>>>>>> ba2837e86b342def917ad6322bb69d3cecff280f
geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]

<<<<<<< HEAD
print("Lat:", lat, "Lon:", lon)

weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
   "latitude": lat,
   "longitude": lon,
   "current_weather": True
}
weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()

print("Temperatura:", weather_data["current_weather"]["temperature"])
=======
print("Lat:", lat, "Lon:", lon)
>>>>>>> ba2837e86b342def917ad6322bb69d3cecff280f
