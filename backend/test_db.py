import db

db.new_list('username@example.com', 'yyy', [])

print(db.get_lists('username@example.com'))

print(db.get_list('username@example.com', 'yyy'))
