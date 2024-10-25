import requests
import json
import time
import datetime

class Station:

    def __init__(self, json_object):
        properties = json_object["properties"]
        self.id = properties["@id"]
        self.type = properties["@type"]
        self.name = properties["name"]
        self.station_id = properties["stationIdentifier"]
        self.forecast_url = properties["forecast"]
        self.json_object = json_object

def get_forecast(json_object):
    url = json_object["properties"]["forecast"]
    resp = requests.get(url)
    return resp.json()

def get_forecast_grid_data(json_object):
    url = json_object["properties"]["forecast"]
    resp = requests.get(url)
    return resp.json()

def get_grid_points(lat, long):
    url = f"https://api.weather.gov/points/{lat},{long}"
    resp = requests.get(url)
    return resp.json()

def print_json(json_object):
    text = json.dumps(json_object, sort_keys=True, indent=4)
    print(text)

def get_stations():
    url = "https://api.weather.gov/stations"
    resp = requests.get(url)
    return resp.json()["observationStations"]

def save_station_file(code, json_obj, form="json"):
    if form != "json":
        print(f"Error: {form} not supported")
   
    ts = time.time()
    t = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
    with open(f"../data/station_{code}_{t}.{form}", 'w', encoding='utf-8') as f:
        json.dump(json_obj, f, ensure_ascii=False, indent=4)

def latest_observation(stationId):
    url = f"https://api.weather.gov/{stationId}/observations/latest"
    resp = requests.get(url)

def station(url):
    resp = requests.get(url)
    return resp.json()

def update_station_list():
    station_list = []
    code_list = []
    for url in get_stations():
        code = url.split("/")[4]
        code_list.append(code)
        print(f"Getting response for station {code} from {url}...")
        station_resp = station(url)
        station_list.append(Station(station_resp))
        save_station_file(code, station_resp)
    print(f"Station files saved: {len(station_list)}")

def main():
    lat = 39.71
    long = -74.22
    update_station_list()

if __name__=='__main__':
    main()
