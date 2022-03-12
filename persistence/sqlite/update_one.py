import sqlite3 as sql

db = sql.connect('users.db')
cursor = db.cursor()

num = int(input("Please the user id: \n"))
cursor.execute(f"SELECT * FROM users WHERE id = {num}")

# to display the records
print("Current user details are as follows: ")
fetch = cursor.fetchone()
data = f"id: {fetch[0]}, \nname: {fetch[1]} \nheight: {fetch[2]} \nweight: {fetch[3]} \ndate_of_birth: {fetch[4]}"
print(data)

# to update the record
change = input("What would you like to change? \n")
change_value = input(f"What is the new value for {change}? \n")

cursor.execute(f"UPDATE users SET {change}={change_value} WHERE id = {num}")
db.commit()

print("The new record has been updated.")
