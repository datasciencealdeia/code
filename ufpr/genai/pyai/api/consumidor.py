import requests

cidade = "Curitiba"

geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
   "name": cidade,
   "count": 1
}
geo_response = requests.get(geo_url, params=geo_params)
weather_params = {
   "latitude": lat,
   "longitude": lon,
   "current_weather": True
}
weather_response = requests.get(weather_url, params=weather_params)

print("Temperatura:", weather_data["current_weather"]["temperature"])
