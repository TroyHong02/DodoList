from flask import Flask, request
from bson import json_util
import db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/signup", methods=['POST'])
def sign_up():
    return 

@app.route("/login", methods=['POST'])
def login():
    return 

@app.route("/logout", methods=['POST'])
def logout():
    return 


"""
json_util.dumps() converts from python dictionary -> json
flask can do this by itself for simple types, but for MongoDB's ObjectIds
special handling is needed
"""

"""
for post requests, data will be sent via a JSON payload + path
access via request.get_json()
note: react server will have to send content type header
"""
@app.route("/newlist", methods=['POST'])
def new_list():
    email = 'username@example.com'
    data = request.get_json()
    if not data:
        return {'success': False, 'message': 'invalid data'}
    title = data.get('title')
    if not title:
        return {'success': False, 'message': 'invalid data'}
    # list always starts with 0 tasks
    return json_util.dumps(db.new_list(email, title))

# TODO: get user from cookie header

"""
for get requests, data will be encoded via path 
i.e /getlist/list-id/
the way you do this in flask is
@app.route('/getlist/type:name')
then
def func(name): ...
"""
@app.route("/getlist/<string:list_id>", methods=['GET'])
def get_list(list_id):
    email = 'username@example.com'
    # in this case, db.get_list returns appropriate json that we can just forward
    return json_util.dumps(db.get_list(email, list_id))


@app.route("/getlists", methods=['GET'])
def get_lists():
    email = 'username@example.com'
    # TODO any processing. (task ids not really needed to send back)
    return json_util.dumps(db.get_lists(email))

"""
for post requests, data will be sent via a JSON payload + path
access via request.get_json()
note: react server will have to send content type header
"""
@app.route("/updatelist/<string:list_id>", methods=['POST'])
def update_list(list_id):
    email = 'username@example.com'
    data = request.get_json()
    if not data:
        return {'success': False, 'message': 'invalid data'}
    newtitle = data.get('title', '')
    if not newtitle:
        return {'success': False, 'message': 'invalid data'}
    # TODO db.update_list(email, list_id, newtitle)

@app.route("/deletelist/<string:list_id>", methods=['POST'])
def delete_list(list_id):
    email = 'username@example.com'
    return json_util.dumps(db.delete_list(email, list_id))

@app.route("/gettask/<string:task_id>", methods=['GET'])
def get_task(task_id):
    email = 'username@example.com'
    return json_util.dumps(db.get_task(email, task_id))

@app.route("/newtask/<string:task_id>", methods=['POST'])
def new_task():
    email = 'username@example.com'
    data = request.get_json()
    if not data:
        return {'success': False, 'message': 'invalid data'}
    list_id = data.get('list_id')
    if not list_id:
        return {'success': False, 'message': 'invalid data'}
    task_name = data.get('task_name')
    if not task_name:
        return {'success': False, 'message': 'invalid data'}
    task_desc = data.get('task_desc')
    if not task_desc:
        return {'success': False, 'message': 'invalid data'}
    due_date = data.get('due_date')
    if not due_date:
        return {'success': False, 'message': 'invalid data'}
    return json_util.dumps(db.new_task(email, list_id, task_name, task_desc, due_date))


@app.route("/updatetask", methods=['POST'])
def update_task():
    return 
    #TODO implement update_task in db

@app.route("/deletetask/<string:task_id>", methods=['POST'])
def delete_task(list_id, task_id):
    email = 'username@example.com'
    return json_util.dumps(db.delete_task(email, list_id, task_id))
