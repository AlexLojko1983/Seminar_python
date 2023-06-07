from sql_class import DataBase

db = DataBase()

# db.create_login()
# db.add('dfasd@tut.by', 'qwerty12345')

print(db.login('dfasd@tut.by', 'qwerty12345'))
print(db.login('dfasd@tut.by', 'qwerty12345dd'))
print(db.login('dfasd@tudt.by', 'qwerty12345'))
