import os
import json
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String

# Define the PostgreSQL connection
DATABASE_URL = "postgresql://user:password@localhost:5432/mydatabase"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def insert_data(table_name, json_data, schema_map):
    # Convert JSON to DataFrame based on the schema_map
    records = []

    for item in json_data:
        if isinstance(item, dict):
            record = {}
            for json_key, column_name in schema_map.items():
                keys = json_key.split('.')
                value = item
                try:
                    for key in keys:
                        if key.startswith('@'):
                            key = key[1:]
                        if key.startswith('$'):
                            key = key[1:]
                        value = value[key]
                    record[column_name] = value
                except KeyError:
                    record[column_name] = None
            
            # Debugging: Print out each record
            print(record)
            records.append(record)

    if records:
        df = pd.DataFrame(records)
        # Convert column names to lowercase
        df.columns = [col.lower() for col in df.columns]
        # Insert DataFrame into the PostgreSQL table
        try:
            df.to_sql(table_name, engine, if_exists='append', index=False)
            print(f"Inserted {len(records)} records into table {table_name}")
        except Exception as e:
            print(f"Error inserting records into table {table_name}: {e}")
    else:
        print(f"No valid records found for table {table_name}")

# Map of JSON file names to table names and schemas
data_files = {
    'aircraft.json': {
        'table': 'aircraft',
        'schema': {
            'AircraftCode': 'aircraft_code',
            'Names.Name.@LanguageCode': 'language_code',
            'Names.Name.$': 'aircraft_name',
            'AirlineEquipCode': 'airline_equip_code'
        }
    },
    # Add other mappings for airlines.json, airports.json, etc.
}

# Base directory where JSON files are stored
base_dir = './collected_data'

def main():
    for file_name, config in data_files.items():
        file_path = os.path.join(base_dir, file_name)
        json_data = load_json(file_path)
        
        # Adjust for the nested structure
        root_key = list(json_data.keys())[0]
        nested_key = list(json_data[root_key].keys())[0]
        data = json_data[root_key][nested_key]['AircraftSummary']
        
        # Debugging: Print the first few records to verify
        print(f"Processing {file_name}:")
        print(json.dumps(data[:3], indent=4))  # Print the first 3 records for verification
        
        insert_data(config['table'], data, config['schema'])

if __name__ == "__main__":
    main()