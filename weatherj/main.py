import requests
import json
import time
import datetime

from station import Station
from utils import get_all_station_ids

_BASE_URL_ = "https://api.weather.gov"

def main():
    stationId = get_all_station_ids()[0]
    station = Station(stationId)

if __name__=='__main__':
    main()
