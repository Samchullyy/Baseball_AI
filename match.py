import pymongo

from pymongo import MongoClient
from pymongo import ReturnDocument
client = MongoClient('mongodb://localhost:27017')
db = client['match']

pymongo.collection.Collection(db, matchID, create=true)

result = db.match.insert_one({'x': i})
result = db.match.insert_many([{'x': i} for i in range(2)])

result = db.match.replace_one({'x': 1}, {'y': 1})
for doc in db.match.find():
    print(doc)

result = db.match.update_one({'x': 1}, {'$inc': {'x': 3}})
result = db.match.update_many({'x': 1}, {'$inc': {'x': 3}})
for doc in db.match.find():
    print(doc)

result = db.match.delete_one({'x': 1})
result = db.match.delete_many({'x': 1})

db.match.find({"hello", "world"})
db.match.find(modifiers={"$maxTimeMS": 500})

db.match.find_one_and_delete({'x': 1}, sort=[('_id', pymongo.DESCENDING)])
db.match.find_one_and_replace({'x': 1}, {'y': 1})
for doc in db.match.find():
    print(doc)

db.match.find_one_and_update({'id': 'userid'}, {'$inc': {'seq': 1}}, return_document=ReturnDocument.AFTER)

{u'_id': 665, u'done': True, u'result': {u'count': 26}}
{u'_id': 701, u'done': True, u'result': {u'count': 17}}
db.test.find_one_and_update({'done': True},{'$set': {'final': True}}, sort=[('_id', pymongo.DESCENDING)])
{u'_id': 701, u'done': True, u'result': {u'count': 17}}


db.match.count({'x': 1})

rename(new_name_collection)

group
