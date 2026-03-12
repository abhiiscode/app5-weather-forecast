import requests

def get_data(place, forecast_days=None, api_key=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    responce = requests.get(url)
    data = responce.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data