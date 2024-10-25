import json as json

from utils import get_station_info

_BASE_URL_ = "https://api.weather.gov"

class Station:
    def __init__(self, stationId):
        self.stationId = stationId.upper()

        data = get_station_info(self.stationId)
        properties = data.get("properties", {})
        self.tz = properties.get("timeZone", {})
        self.name = properties.get("name", {})
        self.countyId = properties.get("county", {}).split('/')[5]
        self.zoneId = properties.get("forecast", {}).split('/')[5]

    def _stationId(self):
        return self.stationId

    def _name(self):
        return self.name

    def _countyId(self):
        return self.countyId

    def _tz(self):
        return self.tz

    def _zoneId(self):
        return self.zoneId 
