import sqlite3

db = sqlite3.connect('users.db')
cursor = db.cursor()

cursor.execute("SELECT * FROM users")

single_record = cursor.fetchone()
print(single_record)

db.close()