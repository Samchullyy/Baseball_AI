import pymongo

from pymongo import MongoClient
from pymongo import ReturnDocument
client = MongoClient('mongodb://localhost:27017')
db = client['player']

pymongo.collection.Collection(db, pid, create=true)