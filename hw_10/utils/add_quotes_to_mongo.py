import json
from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://anton12vasyliev:ofPpZwz5gPOCaTMA@cluster.po4pa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.hw10

with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes = json.load(file)

for quote in quotes:

    author = db.authors.find_one({'fullname': quote['author']})
    print(author)
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
    else:
        print(f"Author {quote['author']} not found in database.")
