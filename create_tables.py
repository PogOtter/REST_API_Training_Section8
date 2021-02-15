import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Integer primary key will ensure ID is set based on avialable row
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

# add a debug entry for the 'items' table
#cursor.execute("INSERT INTO items VALUES('test', 19.99)")

connection.commit()
connection.close()