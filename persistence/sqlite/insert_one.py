import sqlite3 as sql

db = sql.connect('users.db')
cursor = db.cursor()

values = []

name = input("Please enter the name of user: \n")
values.append(name)

height = float(input("Please enter the height (m) of the user: \n"))
values.append(height)

weight = float(input("Please enter the height (kg) of the user: \n"))
values.append(weight)

birth_date = input("Please enter the user's date of birth (yy-mm-dd): \n")
values.append(birth_date)

entry = "INSERT INTO users (name, height, weight, date_of_birth) VALUES (?, ?, ?, ?)"
cursor.execute(entry,values)
db.commit()

print("The record has been added to the database")
print(f"The id is {cursor.lastrowid}.")

db.close()


