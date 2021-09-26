import db

db.new_list('username@example.com', 'yyy', [])

res = db.get_lists('username@example.com')

print(res)

lists = res['data']

for lst in lists:
    print(lst)

lst1_id = lst['_id']

print(db.get_list('username@example.com', lst1_id))

print(db.new_task('username@example.com', lst1_id, 'hello world', 'yo mama', '09/30/21'))

print(db.get_list('username@example.com', lst1_id))
