from pymongo.mongo_client import MongoClient
from fastapi import FastAPI

app = FastAPI()


uri = ""

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("DB connection successfully")
except Exception as e:
    print("Fail to connect DB")
