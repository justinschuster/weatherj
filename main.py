import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_weather(url):
    json_data = None
    response = requests.get(url)
    if response.status_code == 200:
        write_json(response.text)
        json_data = response.json()
        get_temperature(json_data)
    else:
        print("Error", response.status_code)  

    if json_data is None:
        print("Error: json_data is None")
    return json_data

def get_temperature(data):
    x = []
    y = []
    forecasts = data['properties']['periods']
    for i in forecasts:
        #print('{}. {}: {}'.format(i["number"], i['name'], i['temperature']))
        x.append(i['number'])
        y.append(i['temperature'])
    
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Temperature')
    plt.title('Sample')
    plt.savefig('test_data/plots/example.png')
    print('plot saved...')

def write_json(data):
    file = open('test_data/example.json', 'w')
    file.write(data)
    file.close()

def format_data(data):
    coordinates = data['geometry']['coordinates'][0][0]
    latitude = coordinates[0]
    longitude = coordinates[1]
    # print("{}, {}".format(longitude, latitude))
    forecast_data = data['properties']['periods']
    for i in forecast_data:
        i["longitude"] = longitude
        i["latitude"] = latitude
    df = pd.DataFrame(forecast_data)

def save_to_csv(df):
    df.to_csv('test_data/csv/test_data.csv') 

def get_url_points(lat, long):
    url = 'https://api.weather.gov/points/{},{}'.format(lat, long)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_url = data['properties']['forecast']
        return forecast_url
    else:
        print("Error", response.status_code)  
    return None
 
if __name__=='__main__':
    nycLat = 40.71
    nycLong = -74
    url = get_url_points(nycLat, nycLong)
    print(url)
    if url is not None:
        json_data = get_weather(url)
        format_data(json_data)
    else:
        print('Error: url not found')
