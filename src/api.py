from os import write
import requests
import json

def get_gridpoints(lat, long):
    url = 'https://api.weather.gov/points/{},{}'.format(lat, long)
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        return response.json()['properties']['forecast']
    else:
        print("Error", response.status_code)

def get_weather(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        json_data = fix_json_format(json_data)
        data = json.dumps(json_data, indent=4)
        return data
    else:
        print("Error", response.status_code)

def write_to_json_file(data, url):
    url = url.split('/')
    with open(f"src/test_data/json/example-{url[4]}-{url[5]}.json", 'w')  as file:
        file.write(data)
        file.close()

# TODO: Need to add colums for location and other information
def fix_json_format(data):
    for i in data['properties']['periods']:
        i['probabilityOfPrecipitation'] = i['probabilityOfPrecipitation']['value']
        i['dewpoint'] = i['dewpoint']['value']
        i['relativeHumidity'] = i['relativeHumidity']['value']
    return data['properties']['periods']
