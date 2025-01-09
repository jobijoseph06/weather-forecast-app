import requests

API_key = "fe9c39c000107a291744d4b5749ccf41"

def get_data(place, forecast, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_days = 8 * forecast
    filtered_data = filtered_data[:nr_days]
    return filtered_data








if __name__ == "__main__":
   print(get_data(place="chennai", forecast=2, kind="Sky"))


