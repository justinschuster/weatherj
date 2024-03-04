import requests
import matplotlib.pyplot as plt

def get_weather(url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json(response.text)
        data = response.json()
        get_temperature(data)
    else:
        print("Error", response.status_code)  

def get_temperature(data):
    x = []
    y = []
    forecasts = data['properties']['periods']
    for i in forecasts:
        print('{}. {}: {}'.format(i["number"], i['name'], i['temperature']))
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

if __name__=='__main__':
    gridX = 31
    gridY = 80
    url = 'https://api.weather.gov/gridpoints/TOP/{},{}/forecast'.format(gridX, gridY)
    get_weather(url)
