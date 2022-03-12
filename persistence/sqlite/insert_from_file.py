import csv
import sqlite3 as sql

db = sql.connect('users.db')
cursor = db.cursor()

entry = "INSERT INTO users (name, height, weight, date_of_birth) VALUES (?, ?, ?, ?)"

file_path = 'users.csv'
with open(file_path) as file:
    csv_reader = csv.reader(file)
    list_data = []

    for record in csv_reader:
        list_data.append(record)

for values in list_data:
    cursor.execute(entry, values)
db.commit()

