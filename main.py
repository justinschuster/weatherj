import requests

url = 'https://api.weather.gov/points/39,-74'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['properties']) 
else:
    print("Error", response.status_code)
