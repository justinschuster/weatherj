import json
import requests
import time
import datetime

_BASE_URL_ = "https://api.weather.gov"

def get_station_info(stationId):
    data = requests.get(f"{_BASE_URL_}/stations/{stationId}")
    data = data.json() 
    return data

def get_all_station_ids():
    all_stations = []
    cursor = None
    page = 1

    headers = {
        "User-Agent": "(weatherj, schujustin@gmail.com)"
    } 

    station_count = 0
    while True:
        try:
            if page == 5: break; # for testing
            url = f"{_BASE_URL_}/stations"

            if cursor:
                #url = f"{url}/?cursor={cursor}"
                url = cursor

            data = requests.get(url, headers=headers)
            data = data.json() 

            stations = data.get("observationStations", [])
            for station in stations:
                stationId = station.split("/")[4]
                if stationId not in all_stations:
                    all_stations.append(stationId)

            pagination = data.get("pagination", {})
            next_cursor = pagination.get("next")

            if not next_cursor:
                print("Reached end of pagination")
                break

            if station_count == len(all_stations):
                break
            else:
                station_count = len(all_stations)

            cursor = next_cursor
            page += 1
            time.sleep(0.5)

        except requests.RequestException as e:
            print(f"Error fetching page {page}: {str(e)}")
            time.sleep(2)
            continue

    print(f"Total stations fetch: {len(all_stations)}")
    return all_stations

def print_json(json_object):
    text = json.dumps(json_object, sort_keys=True, indent=4)
    print(text)

def save_station_file(code, json_obj, form="json"):
    if form != "json":
        print(f"Error: {form} not supported")

    ts = time.time()
    t = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
    with open(f"/home/justin/projects/weatherj/data/station_{code}_{t}.{form}", 'w', encoding='utf-8') as f:
        json.dump(json_obj, f, ensure_ascii=False, indent=4)
