from pymongo import MongoClient
from decouple import config

client = MongoClient(
    config('MONGO_URI'),
    username=config('MONGO_USER'),
    password=config('MONGO_PASSWORD'),
    authSource='admin'
)

db = client[config('MONGO_DB')]


def custom_response(success=True, payload=None, error=None, status=200):
    response = {'success': success}
    if success:
        response['payload'] = payload
    else:
        response['error'] = error

    return response, status
