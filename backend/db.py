from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['dodolist']
collection = db['userdata']

def new_list(email, list_name, tasks):
    collection.update({'email': email}, {'$push': {'lists': {
        'list_name': list_name,
        'tasks': tasks,
    }}})

def get_list(email, list_name):
    user = collection.find_one({'email': email, 'lists': {'$elemMatch': {'list_name': list_name}}})
    if not user:
        return 'not found'
    for lst in user['lists']:
        if lst['list_name'] == list_name:
            return lst

    return 'not found'

def get_lists(email):
    return collection.find_one({'email': email})['lists'];
    
