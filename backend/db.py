from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['dodolist']
users = db['users']
"""
users {
    email: str
    password: str
    lists: [objectIds]
}
"""

lists = db['lists']
"""
lists {
    owner: objectId
    list_name: str
    tasks: [objectIds]
}
"""

tasks = db['tasks']
"""
tasks {
    task_name: str
    task_desc: str
    due_date: time
    status: str
    list: objectId
    owner: objectId # TODO needed?
}
"""


# TODO can merge new_list and update list to update with upsert = true
# unique list name as key..
def new_list(email, list_name, tasks):
    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}
    
    owner = user['_id']

    res = lists.insert_one({
        'owner': owner,
        'list_name': list_name,
        'tasks': tasks,
    })

    return {'success': True, 'message': 'new list created'}

def get_list(email, list_name):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}
    
    owner = user['_id']

    res = lists.find_one({'owner': owner, 'list_name': list_name})
    # if not res:
    #     return {'success': False, 'message': 'list not found'}

    return {'success': True, 'data': res}

def get_lists(email):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}
    
    owner = user['_id']

    res = lists.find({'owner': owner})

    return {'success': True, 'data': list(res)}
    
