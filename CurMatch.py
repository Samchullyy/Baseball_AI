import pymongo

from pymongo import MongoClient
from pymongo import ReturnDocument
client = MongoClient('mongodb://localhost:27017')
db = client['CurMatch']

pymongo.collection.Collection(db, season, create=true)