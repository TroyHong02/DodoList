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
# unique list name as key..

# TODO 2 get list id before insert, then update user once, instead of finding -> list insert -> update
def new_list(email, list_name, tasks):

    user = users.find_one({'email': email})
    if not user:
        return {'success': False, 'message': 'user not found'}

    print(user)
    user_id = user['_id']

    res = lists.insert_one({
        'list_name': list_name,
        'tasks': tasks,
    })

    _id = res.inserted_id

    # TODO unique array needed?
    users.update({'_id': user_id}, {
        '$push': { 'lists': _id }
    })

    print(user)
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

    print(user)

    res = [None] * len(user['lists'])

    for i in range(len(user['lists'])):
        _id = user['lists'][i]
        res[i] = lists.find_one({'_id': _id})
    
    return {'success': True, 'data': list(res)}


def new_task(email, list_id, task_name, task_desc, due_date):
#WORK IN PROGRESS!!!!!! STUCK ON TASKS: What is task when you initialize a list? []? the tasks object? (didnt work before), need to review documentation!
    print('a')
    user = users.find_one({'email': email})
    if not user:
        print('new_task')
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
    print(res)
    return {'success': True, 'message': 'task successfully created'}
