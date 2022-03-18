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
    while count < len(records):
        print(f"Product name: {records[count][1]}\nDescription: {records[count][2]}\nStock level: {records[count][3]}")
        print()
        count = count + 1


def display_product_supplier():
    cursor.execute("""
    SELECT * FROM product p
    INNER JOIN supplier s
    ON p.product_id = s.supplier_id 
    """)

    records = cursor.fetchall()
    print("The suppliers for each product are as follows: ")
    print()

    count = 0
    while count < len(records):
        print(f"Product: {records[count][1]}, Supplier: {records[count][4]}")
        count = count + 1


