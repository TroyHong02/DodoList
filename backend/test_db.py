import db

db.new_list('username@example.com', 'yyy', [])

res = db.get_lists('username@example.com')

print(res)

lists = res['data']

for lst in lists:
    print(lst)

lst1_id = lst['_id']

print(db.get_list('username@example.com', lst1_id))

new_task1 = db.new_task('username@example.com', lst1_id, 'hello world', 'yo mama', '09/30/21')

print(new_task1)

tasks = db.get_tasks('username@example.com', lst1_id)['data']

print(tasks)

task1_id = tasks[0]['_id']

task1 = db.get_task('username@example.com', task1_id)

#new_task2 = new_task1? possibly related to the need of unique array mentionted in db.py @line 114?   
#
# new_task2 = db.new_task('username@example.com', lst1_id, 'goodbye world', 'yote', '1337')
#
# print(new_task2)

print(tasks)

# del_task1 = db.delete_task('username@example.com', lst1_id, task1_id)

# print(del_task1)

# tasks_after_del = db.get_tasks('username@example.com', lst1_id)['data']

# print(tasks_after_del)


del_list = db.delete_list('username@example.com', lst1_id)

print(del_list)

after_del_list = db.get_lists('username@example.com')

#lists += None everytime this file is run. Error? or not?!?
print('lists = ', after_del_list['data'])
# for task in 

# task1_id = db.get_task('username@example.com', res)

# print(db.get_list('username@example.com', lst1_id))

# print(db.get_task('username@example.com', lst1_id))