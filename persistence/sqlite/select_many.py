import sqlite3 as sql

db = sql.connect('users.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM users")

try:
    entry = int(input("How many entries do you want to be displayed? \n"))
    print()
    if (entry >= 1) and (entry <= 3):
        no_records = cursor.fetchmany(entry)
        print(f"Displaying {entry} records:")
        for records1 in no_records:
            print(records1)
    else:
        all_records = cursor.fetchall()
        print("Displaying all records: ")
        for records2 in all_records:
            print(records2)

except ValueError:
    print("Please enter a number")

db.close()

