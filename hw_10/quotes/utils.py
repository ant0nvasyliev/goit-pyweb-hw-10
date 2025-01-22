from pymongo import MongoClient
from pymongo.server_api import ServerApi


client = None

def get_mongodb():
    global client
    if not client:
        uri = "mongodb+srv://anton12vasyliev:ofPpZwz5gPOCaTMA@cluster.po4pa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(uri, server_api=ServerApi('1'))
    return client.hw10

