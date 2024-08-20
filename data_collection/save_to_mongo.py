import pymongo
import os
import json
from pymongo import MongoClient

# MongoDB connection setup
MONGO_URI = 'mongodb://localhost:27017'
DATABASE_NAME = 'json_data_db'

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

def save_json_to_mongo(filename):
    with open(filename) as f:
        data = json.load(f)
        collection_name = os.path.splitext(os.path.basename(filename))[0]
        collection = db[collection_name]
        collection.insert_many(data if isinstance(data, list) else [data])
        print(f"Data from {filename} saved to MongoDB collection {collection_name}")

# Example usage
for table in ['aircraft', 'airports', 'airlines', 'cities', 'countries']:
    save_json_to_mongo(f'collected_data/{table}.json')