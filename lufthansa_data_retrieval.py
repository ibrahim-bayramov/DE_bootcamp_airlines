import requests
import json

# Authentication details
CLIENT_ID = 'tugz7s9hv4ay8gahfv5uu7zmu'
CLIENT_SECRET = 'GgDFWJQ37R'
ACCESS_TOKEN = 'ww2sdn55j7f5xzqepdvjmuxv'

# Base URL
BASE_URL = 'https://api.lufthansa.com/v1/'

# Headers
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/json'
}

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_countries():
    url = f'{BASE_URL}mds-references/countries'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'countries.json')
        print("Countries data saved to countries.json")
    else:
        print(f"Failed to retrieve countries: {response.status_code}")

get_countries()

def get_cities():
    url = f'{BASE_URL}mds-references/cities'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'cities.json')
        print("Cities data saved to cities.json")
    else:
        print(f"Failed to retrieve cities: {response.status_code}")

get_cities()

def get_airports():
    url = f'{BASE_URL}mds-references/airports'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'airports.json')
        print("Airports data saved to airports.json")
    else:
        print(f"Failed to retrieve airports: {response.status_code}")

get_airports()

def get_airlines():
    url = f'{BASE_URL}mds-references/airlines'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'airlines.json')
        print("Airlines data saved to airlines.json")
    else:
        print(f"Failed to retrieve airlines: {response.status_code}")

get_airlines()

def get_aircraft():
    url = f'{BASE_URL}mds-references/aircraft'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'aircraft.json')
        print("Aircraft data saved to aircraft.json")
    else:
        print(f"Failed to retrieve aircraft: {response.status_code}")

get_aircraft()
