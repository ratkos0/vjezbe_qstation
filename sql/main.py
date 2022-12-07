import sqlite3

connection = sqlite3.connect('qbase.db')

cursor = connection.cursor()

sql_command = """CREATE TABLE clanovi(\
id INTEGER PRIMARY KEY,\
first_name VARCHAR(20),\
last_name VARCHAR(20),\
pol CHAR(1),\
godine VARCHAR(2));"""

cursor.execute(sql_command)

connection.close()
