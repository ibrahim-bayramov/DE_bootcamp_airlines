import requests
import json
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file in the root directory
load_dotenv()

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
    
    elif table_name == 'airports':
        for item in data['Airports']:
            cur.execute("""
                INSERT INTO airports (airport_code, latitude, longitude, city_code, country_code, location_type, name, utc_offset, timezone_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (airport_code) DO NOTHING;
            """, (item['AirportCode'], item.get('Latitude'), item.get('Longitude'), item.get('CityCode'), item.get('CountryCode'),
                  item.get('LocationType'), item.get('Name'), item.get('UtcOffset'), item.get('TimezoneId')))
    
    elif table_name == 'airlines':
        for item in data['Airlines']:
            cur.execute("""
                INSERT INTO airlines (airline_id, airline_id_icao, name)
                VALUES (%s, %s, %s)
                ON CONFLICT (airline_id) DO NOTHING;
            """, (item['AirlineId'], item.get('AirlineIdIcao', ''), item['Name']))
    
    elif table_name == 'cities':
        for item in data['Cities']:
            cur.execute("""
                INSERT INTO cities (city_code, country_code, utc_offset, timezone_id, names, airports, meta)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (city_code) DO NOTHING;
            """, (item['CityCode'], item.get('CountryCode'), item.get('UtcOffset'), item.get('TimezoneId'), 
                  json.dumps(item.get('Names', {})), json.dumps(item.get('Airports', [])), json.dumps(item.get('Meta', {}))))
    
    elif table_name == 'countries':
        for item in data['Countries']:
            cur.execute("""
                INSERT INTO countries (country_code, names, meta)
                VALUES (%s, %s, %s)
                ON CONFLICT (country_code) DO NOTHING;
            """, (item['CountryCode'], json.dumps(item.get('Names', {})), json.dumps(item.get('Meta', {}))))
    
    conn.commit()
    cur.close()
    conn.close()

# Retrieve and save data
get_data('mds-references/countries', 'countries.json')
get_data('mds-references/cities', 'cities.json')
get_data('mds-references/airports', 'airports.json')
get_data('mds-references/airlines', 'airlines.json')
get_data('mds-references/aircraft', 'aircraft.json')

# Save data to the database
for table in ['aircraft', 'airports', 'airlines', 'cities', 'countries']:
    with open(os.path.join(COLLECTED_DATA_DIR, f'{table}.json')) as f:
        data = json.load(f)
        save_to_db(data, table)