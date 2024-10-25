from station import Station
from utils import get_all_station_ids

def main():
    stationId = get_all_station_ids()[0]
    station = Station(stationId)

if __name__=='__main__':
    main()
