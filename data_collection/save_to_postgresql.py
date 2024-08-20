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

# Process the JSON file and extract relevant data
def process_json(file_path, table_name):
    json_data = load_json(file_path)
    aircraft_data = json_data['AircraftResource']['AircraftSummaries']['AircraftSummary']

    # Extract relevant fields
    records = []
    for item in aircraft_data:
        record = {
            'aircraft_code': item['AircraftCode'],
            'aircraft_name': item['Names']['Name']['$'],
            'airline_equip_code': item['AirlineEquipCode']
        }
        records.append(record)

    # Insert records into the database
    if records:
        insert_data(table_name, records)
    else:
        print(f"No valid records found in {file_path}")

# Main execution function
def main():
    base_dir = './collected_data'
    file_name = 'aircraft.json'
    file_path = os.path.join(base_dir, file_name)
    
    print(f"Processing {file_name}...")
    process_json(file_path, 'aircraft')

if __name__ == "__main__":
    main()