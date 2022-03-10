import sqlite3 as sql

db = sql.connect('users.db')  # to connect to the database
cursor = db.cursor()  # to execute the query and fetch all the records from the database

cursor.execute("SELECT * FROM users")
all_records = cursor.fetchall()

print("All users in the system: ")
print()

for records in all_records:
    print(records)

db.close()  # to close the database
