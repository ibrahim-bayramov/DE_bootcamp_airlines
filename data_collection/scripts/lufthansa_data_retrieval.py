import requests
import json
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file in the root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

# Authentication details
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# Base URL
BASE_URL = 'https://api.lufthansa.com/v1/'

# Headers
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Accept': 'application/json'
}

# Directory to save the collected data
COLLECTED_DATA_DIR = os.path.join(os.path.dirname(__file__), '../collected_data')

def save_json(data, filename):
    # Ensure the collected_data directory exists
    os.makedirs(COLLECTED_DATA_DIR, exist_ok=True)
    filepath = os.path.join(COLLECTED_DATA_DIR, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_countries():
    url = f'{BASE_URL}mds-references/countries'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'countries.json')
        print("Countries data saved to collected_data/countries.json")
    else:
        print(f"Failed to retrieve countries: {response.status_code}")

def get_cities():
    url = f'{BASE_URL}mds-references/cities'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'cities.json')
        print("Cities data saved to collected_data/cities.json")
    else:
        print(f"Failed to retrieve cities: {response.status_code}")

def get_airports():
    url = f'{BASE_URL}mds-references/airports'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'airports.json')
        print("Airports data saved to collected_data/airports.json")
    else:
        print(f"Failed to retrieve airports: {response.status_code}")

def get_airlines():
    url = f'{BASE_URL}mds-references/airlines'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'airlines.json')
        print("Airlines data saved to collected_data/airlines.json")
    else:
        print(f"Failed to retrieve airlines: {response.status_code}")

def get_aircraft():
    url = f'{BASE_URL}mds-references/aircraft'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        save_json(data, 'aircraft.json')
        print("Aircraft data saved to collected_data/aircraft.json")
    else:
        print(f"Failed to retrieve aircraft: {response.status_code}")

def save_to_db(data, table_name):
    DATABASE_URL = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    if table_name == 'aircraft':
        for item in data['AircraftResource']['AircraftSummaries']['AircraftSummary']:
            cur.execute("""
                INSERT INTO aircraft (aircraft_code, name, airline_equip_code)
                VALUES (%s, %s, %s)
                ON CONFLICT (aircraft_code) DO NOTHING;
            """, (item['AircraftCode'], item['Names']['Name']['$'], item.get('AirlineEquipCode', '')))
    
    conn.commit()
    cur.close()
    conn.close()

# Retrieve and save data
get_countries()
get_cities()
get_airports()
get_airlines()
get_aircraft()

# Save data to the database
if aircraft_data:
    save_to_db(aircraft_data, 'aircraft')