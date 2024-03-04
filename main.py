import requests

def get_weather(url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json(response.text)
        data = response.json()
    else:
        print("Error", response.status_code)  

def write_json(data):
    file = open('test_data/example.json', 'w')
    file.write(data)
    file.close()

if __name__=='__main__':
    long = 39
    lat = -74
    url = 'https://api.weather.gov/points/{},{}'.format(long, lat)
    get_weather(url)
