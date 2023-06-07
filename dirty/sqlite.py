import sqlite3

connection = sqlite3.connect('newdb.db')
cur = connection.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS user
            (user_id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, 
            tg_id INTEGER, comment TEXT)''')
connection.commit()
# connection.close()

def add_user(name: str, telegram: int, comment: str):
    cur.execute('''INSERT INTO user (user_name, tg_id, comment) VALUES (?, ?, ?) ''',(name,telegram,comment))
    connection.commit()
    connection.close()
def load_user(name:str)-> list[tuple]:
    data = cur.execute('''SELECT user_name, comment FROM user WHERE user_name=?''',(name,)).fetchall()
    connection.close()
    return data
def update_user(name: str, telegram: int, comment: str, user_id)->None:
    cur.execute('''UPDATE user SET user_name=?, tg_id=?, comment=? WHERE user_id=?''',
                (name, telegram, comment, user_id))
    connection.commit()

def delete_user(user_id: int)-> None:
    cur.execute('''DELETE FROM user WHERE user_id=?''', (user_id,))
    connection.commit()

# add_user('Sania', 46538, 'SUPER')
update_user('Alex', 80336223818, 'Da Da', 1)
delete_user(1)
user_data = load_user('Alex')
print(user_data)