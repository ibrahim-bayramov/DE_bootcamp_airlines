from pymongo import MongoClient


client = pymongo.MongoClient(
    host="127.0.0.1",
    port = 27017,
    username = 'your_user',
    password = 'your_password'

)

db = client["airlines"]  
#collection = db["aircraft"] 

collection_names = db.list_collection_names()

print(collection_names)

client.close()