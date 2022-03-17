import sqlite3 as sql

db = sql.connect("catalogue.db")
cursor = db.cursor()

def display_products_with_stock_levels():
    cursor.execute(
        """SELECT * FROM product
            NATURAL JOIN stock
         """
    )

    records = cursor.fetchall()
    print(f"There are {len(records)} records in the catalogue\nThe stock level for each product is as follows:\n")

    count = 0
    while count < 10:
        print(f"Product name: {records[count][1]}\nDescription: {records[count][2]}\nStock level: {records[count][3]}")
        print()
        count = count + 1
