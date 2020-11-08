from pymongo import MongoClient
from decouple import config

client = MongoClient(
    config('MONGO_URI'),
    username=config('MONGO_USER'),
    password=config('MONGO_PASSWORD'),
    authSource='admin'
)

db = client[config('MONGO_DB')]
