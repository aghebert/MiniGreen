import pymongo

from pymongo import MongoClient
client = MongoClient()

db = client['testme']


print(db)

posts = db.myNewCollection
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)

x = posts.find_one()
print(x)