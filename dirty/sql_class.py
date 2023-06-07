import sqlite3


class DataBase:
    def __init__(self, path: str = 'newdb.db'):
        self.db_path = path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, params: tuple = tuple(), fetchone: bool = False,
                fetchall: bool = False, commit: bool = False):
        connection = self.connection
        cursor = connection.cursor()
        data = ''
        cursor.execute(sql, params)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_login(self):
        sql = '''CREATE TABLE IF NOT EXISTS login_table(user_id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, 
         password TEXT)'''
        self.execute(sql, commit=True)

    def add(self, email: str, password: str):
        sql = '''INSERT INTO login_table (email, password) VALUES (?, ?)'''
        self.execute(sql, (email, password), commit=True)

    def login(self, email: str, password: str):
        sql = '''SELECT email, password FROM login_table WHERE email=?'''
        user = self.execute(sql, (email,), fetchone=True)
        if user:
            if user[1] == password:
                return 'yes'
            else:
                return 'Invalid password!!'
        return 'Invalid e-mail!!'
