import sqlite3 as sql

db = sql.connect('users.db')
cursor = db.cursor()

cursor.execute("SELECT * FROM users")
all_records = cursor.fetchall()

print("All users in the system")
for record in all_records:
    print(record)

db.close()