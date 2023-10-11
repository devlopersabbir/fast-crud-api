import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

mongodbPassword = os.environ.get("MONGODB_PASSWORD")
mongodbUsername = os.environ.get("MONGODB_USERNAME")
mongodbConnectionUrl = f"mongodb+srv://{mongodbUsername}:{mongodbPassword}@cluster0.bplr1gn.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongodbConnectionUrl)

dbs = client.movie_api
usersCollection = dbs["users"]
movieCollection = dbs["movies"]
