import requests

cidade = "Curitiba"
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
    "name": cidade,
    "count": 1
}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]

print("Lat:", lat, "Lon:", lon)