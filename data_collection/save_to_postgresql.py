import os
import json
import pandas as pd
from sqlalchemy import create_engine, MetaData

# Define the PostgreSQL connection
DATABASE_URL = "postgresql://user:password@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to insert data into PostgreSQL
def insert_data(table_name, records):
    df = pd.DataFrame(records)
    df.columns = [col.lower() for col in df.columns]  # Convert column names to lowercase

    # Insert DataFrame into the PostgreSQL table
    try:
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Inserted {len(records)} records into table {table_name}")
    except Exception as e:
        print(f"Error inserting records into table {table_name}: {e}")

# Function to process the JSON and extract relevant fields
def process_json(file_path, table_name, record_extractor):
    json_data = load_json(file_path)
    records = record_extractor(json_data)
    
    # Insert records into the database
    if records:
        insert_data(table_name, records)
    else:
        print(f"No valid records found in {file_path}")

# Extractors for each JSON file type
def extract_aircraft_records(json_data):
    aircraft_data = json_data['AircraftResource']['AircraftSummaries']['AircraftSummary']
    return [
        {
            'aircraft_code': item['AircraftCode'],
            'aircraft_name': item['Names']['Name']['$'],
            'airline_equip_code': item['AirlineEquipCode']
        }
        for item in aircraft_data
    ]

def extract_airlines_records(json_data):
    airline_data = json_data['AirlineResource']['Airlines']['Airline']
    return [
        {
            'airline_id': item['AirlineID'],
            'airline_id_icao': item.get('AirlineID_ICAO', None),
            'airlines_name': item['Names']['Name']['$']
        }
        for item in airline_data
    ]

def extract_airports_records(json_data):
    airport_data = json_data['AirportResource']['Airports']['Airport']
    records = []
    
    for item in airport_data:
        # Check if 'Names' contains a list or a single dictionary
        name_entries = item['Names']['Name']
        if isinstance(name_entries, list):
            # Filter for the English language name
            airport_name = next((name['$'] for name in name_entries if name['@LanguageCode'] == 'EN'), None)
        else:
            # If it's not a list, assume it's already the dictionary we want
            airport_name = name_entries['$'] if name_entries['@LanguageCode'] == 'EN' else None

        record = {
            'airport_code': item['AirportCode'],
            'latitude': item['Position']['Coordinate']['Latitude'],
            'longitude': item['Position']['Coordinate']['Longitude'],
            'city_code': item['CityCode'],
            'country_code': item['CountryCode'],
            'location_type': item['LocationType'],
            'airport_name': airport_name,
            'utc_offset': item.get('UtcOffset', None),
            'time_zone_id': item.get('TimeZoneId', None)
        }
        records.append(record)
    
    return records

def extract_cities_records(json_data):
    city_data = json_data['CityResource']['Cities']['City']
    records = []
    for item in city_data:
        name_entries = item['Names']['Name']
        if isinstance(name_entries, list):
            city_name = next((name['$'] for name in name_entries if name['@LanguageCode'] == 'EN'), None)
        else:
            city_name = name_entries['$'] if isinstance(name_entries, dict) and name_entries.get('@LanguageCode') == 'EN' else name_entries
        records.append({
            'city_code': item['CityCode'],
            'country_code': item['CountryCode'],
            'city_name': city_name,
            'utc_offset': item.get('UtcOffset', None),
            'time_zone_id': item.get('TimeZoneId', None)
        })
    return records

def extract_countries_records(json_data):
    country_data = json_data['CountryResource']['Countries']['Country']
    return [
        {
            'country_code': item['CountryCode'],
            'country_name': next(name['$'] for name in item['Names']['Name'] if name['@LanguageCode'] == 'EN')
        }
        for item in country_data
    ]

# Mapping of files to their corresponding table names and record extractors
file_configs = {
    'aircraft.json': ('aircraft', extract_aircraft_records),
    'airlines.json': ('airlines', extract_airlines_records),
    'airports.json': ('airports', extract_airports_records),
    'cities.json': ('cities', extract_cities_records),
    'countries.json': ('countries', extract_countries_records),
}

# Main execution function
def main():
    base_dir = './collected_data'
    
    for file_name, (table_name, record_extractor) in file_configs.items():
        file_path = os.path.join(base_dir, file_name)
        
        print(f"Processing {file_name}...")
        process_json(file_path, table_name, record_extractor)

if __name__ == "__main__":
    main()