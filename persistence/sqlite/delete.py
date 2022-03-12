import sqlite3 as sql

db = sql.connect('users.db')
cursor = db.cursor()

num = int(input("Please the user id: \n"))
cursor.execute(f"SELECT * FROM users WHERE id = {num}")

# to display the records
print("The following record has been found: ")
fetch = cursor.fetchone()
data = f"id: {fetch[0]}, \nname: {fetch[1]} \nheight: {fetch[2]} \nweight: {fetch[3]} \ndate_of_birth: {fetch[4]}"
print(data)

# delete record
cursor.execute(f"DELETE FROM users WHERE id={num}")
db.commit()
print("The record has been removed.")

db.close()
