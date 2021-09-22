from flask import Flask
import couchbase.subdocument as SD

# needed for any cluster connection
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

# needed to support SQL++ (N1QL) query
from couchbase.cluster import QueryOptions

# get a reference to our cluster
cluster = Cluster('couchbase://localhost', ClusterOptions(
  PasswordAuthenticator('DodoMan', 'p@ssw0rd')))

# get a reference to our bucket
cb = cluster.bucket('users')

# collection
coll = cb.collection('user_data')



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
    coll.mutate_in(user, [SD.array_append('lists', {
                'list_name' : list_name, 
                'tasks' : tasks
            }
        )]
    )
    print('new_list has ran')

@app.route("/getlist", methods=['GET'])
def get_list():
    return 

@app.route("/getlists", methods=['GET'])
def get_lists():
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