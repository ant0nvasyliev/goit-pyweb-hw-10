from django.conf import settings
from pymongo import MongoClient
from pymongo.server_api import ServerApi


client = None

def get_mongodb():
    global client
    if not client:
        uri = settings.MONGODB_URI
        client = MongoClient(uri, server_api=ServerApi('1'))
    return client.hw10

