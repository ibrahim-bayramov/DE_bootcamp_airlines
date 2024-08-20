import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the root directory
load_dotenv()

# Authentication details
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# Base URL
BASE_URL = 'https://api.lufthansa.com/v1/'

# Headers
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/json'
}

# Directory to save the collected data
COLLECTED_DATA_DIR = 'collected_data'

def save_json(data, filename):
    # Ensure the collected_data directory exists
    os.makedirs(COLLECTED_DATA_DIR, exist_ok=True)
    filepath = os.path.join(COLLECTED_DATA_DIR, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_data(endpoint, filename):
    url = f'{BASE_URL}{endpoint}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, filename)
        print(f"{filename} data saved to {COLLECTED_DATA_DIR}/{filename}")
    else:
        print(f"Failed to retrieve {endpoint}: {response.status_code}")

# Retrieve and save data
get_data('mds-references/countries', 'countries.json')
get_data('mds-references/cities', 'cities.json')
get_data('mds-references/airports', 'airports.json')
get_data('mds-references/airlines', 'airlines.json')
get_data('mds-references/aircraft', 'aircraft.json')