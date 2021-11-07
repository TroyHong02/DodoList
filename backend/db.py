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
    list_name: str
    tasks: [objectIds]
}
"""

tasks = db['tasks']
"""
tasks {
    task_name: str
    task_desc: str
    inserted_time: time
    due_date: time
    status: str
}
"""


# TODO can merge new_list and update list to update with upsert = true

# TODO 2 get list id before insert, then update user once, instead of finding -> list insert -> update
def new_list(email, list_name):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}

    user_id = user['_id']

    res = lists.insert_one({
        'list_name': list_name,
        'tasks': [],
    })

    _id = res.inserted_id

    # TODO unique array needed?
    users.update({'_id': user_id}, {
        '$push': { 'lists': _id }
    })

    return {'success': True, 'message': 'new list created'}

def get_list(email, id):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}
    
    res = lists.find_one({'_id': id})
    # if not res:
    #     return {'success': False, 'message': 'list not found'}

    return {'success': True, 'data': res}

def get_lists(email):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}

    res = [None] * len(user['lists'])

    for i in range(len(user['lists'])):
        _id = user['lists'][i]
        res[i] = lists.find_one({'_id': _id})
    
    return {'success': True, 'data': list(res)}


def new_task(email, list_id, task_name, task_desc, due_date):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}
    
    lst = lists.find_one({'_id' : list_id})
    if not lst:
        return {'success': False, 'message': 'list not found'}
    
    new_task = {
        "task_name": task_name,
        "task_desc": task_desc,
        "inserted_time": 'yo mama',
        "due_date": due_date,
        "status": 'yo papa'
    }
        
    res = tasks.insert_one(new_task)

    _id = res.inserted_id

    # TODO unique array needed?
    lists.update({'_id': list_id}, {
        '$push': { 'tasks': _id }
    })

    return {'success': True, 'message': 'task successfully created'}

def get_task(email, task_id):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}
    

    res = tasks.find_one({'_id': task_id})
    if not res:
        return {'success': False, 'message': 'task not found'}

    return {'success': True, 'data': res}

def get_tasks(email, list_id):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}

    lst = lists.find_one({'_id': list_id})
    if not lst:
        return {'success': False, 'message': 'list not found'}

    res = [None] * len(lst['tasks'])

    for i in range(len(lst['tasks'])):
        _id = lst['tasks'][i]
        res[i] = tasks.find_one({'_id': _id})
    
    return {'success': True, 'data': list(res)}

#TODO def update_task():

def delete_task(email, list_id, task_id):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}

    lst = lists.find_one({'_id': list_id})
    if not lst:
        return {'success': False, 'message': 'list not found'}
    
    task = tasks.find_one({'_id': task_id})
    if not task:
        return{'success': False, 'message': 'task not found'}
    
    tasks.delete_one({'_id': task_id})

    return {'success': True, 'message': 'task successfully deleted'}

def delete_list(email, list_id):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}

    lst = lists.find_one({'_id': list_id})
    if not lst:
        return {'success': False, 'message': 'list not found'}

    res = users.update({'_id': user['_id']}, {
        '$pull': {'lists': list_id}
    })
    #TODO interpret res / error handling
    
    task_ids = lst['tasks']
    for task_id in task_ids:
        # we dont really want to call delete_task here, there
        # are certain guarantees that we have here that we shouldnt 
        # bother checking again. i.e list existing
        res = tasks.delete_one({'_id': task_id})
    
    res = lists.delete_one({'_id': list_id})

    return {'success': True, 'message': 'list successfully deleted'}


