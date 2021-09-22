from flask import Flask
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

@app.route("/newlist", methods=['POST'])
def new_list():
    user = 'username'
    list_name = 'xxx'
    tasks = []
    db.new_list(username, list_name, tasks)
    print('new_list has ran')

@app.route("/getlist", methods=['GET'])
def get_list():
    list_name = 'xxx'
    db.get_list(list_name)
    return 

@app.route("/getlists", methods=['GET'])
def get_lists():
    db.get_lists()
    return 

@app.route("/updatelist", methods=['POST'])
def update_list():
    return 

@app.route("/deletelist", methods=['POST'])
def delete_list():
    return 

@app.route("/gettask", methods=['GET'])
def get_task():
    return 

@app.route("/newtask", methods=['POST'])
def new_task():
    return 

@app.route("/updatetask", methods=['POST'])
def update_task():
    return 

@app.route("/deletetask", methods=['POST'])
def delete_task():
    return 

new_list()
