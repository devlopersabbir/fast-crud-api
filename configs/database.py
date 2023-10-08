from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://devlopersabbir:LFRGM936UAARIQ2v@cluster0.bplr1gn.mongodb.net/?retryWrites=true&w=majority")

db = client.movie_api
collectionName = db["user"]
collectionName = db["post"]
