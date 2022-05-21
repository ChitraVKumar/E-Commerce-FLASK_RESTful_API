from multiprocessing import connection
import sqlite3

from colorama import Cursor

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'Chitra', 'fcuk')
insert_query = "INSERT INTO users VALUEs (?, ?, ?)"
cursor.execute(insert_query, user)

users = [(2, 'Edwine', 'abcd'), (3, 'Siva', 'xyz')]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()