from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['dodolist']
collection = db['users']

default_user = {
    'email': 'username@example.com',
    'password': 'abcdef',
    'lists': [],
}

collection.insert_one(default_user)

# find user
res = collection.find_one({'email': 'username@example.com'})
print(res)


#collection.update(


