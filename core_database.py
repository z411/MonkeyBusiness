from pymongo import MongoClient

client = MongoClient("localhost", 27017)

def get_db():
    return client.monkeydb
