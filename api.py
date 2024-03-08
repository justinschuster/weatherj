from os import write
import requests
import json

test_url = 'https://api.weather.gov/gridpoints/OKX/33,35/forecast'

def get_weather(url):
    json_data = None
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        json_data = json_data['properties']['periods']
        data = json.dumps(json_data, indent=4)
        return data
    else:
        print("Error", response.status_code)  


def write_to_json_file(data):
    file = open('test_data/example.json', 'w')
    file.write(data)
    file.close()

data = get_weather(test_url)
write_to_json_file(data)
