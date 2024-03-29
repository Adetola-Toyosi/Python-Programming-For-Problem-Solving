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


def display_product_supplier_locations():
    cursor.execute("""
    SELECT * FROM product p 
    INNER JOIN supplier s 
    ON p.product_id = s.supplier_id
    INNER JOIN location l 
    ON p.product_id = l.id
    """)

    records = cursor.fetchall()

    count = 0
    while count < len(records):
        print(f"Product: {records[count][1]}, Supplier: {records[count][4]}, Supplier Location: {records[count][8]}, {records[count][9]}")
        count = count + 1


def display_products_missing_suppliers():
    cursor.execute("""
    SELECT * FROM product p 
    LEFT OUTER JOIN supplier s 
    ON p.product_id = s.supplier_id
    LEFT OUTER JOIN location l 
    ON p.product_id = l.id
    """)

    records = cursor.fetchall()
    print("The suppliers for each products are: ")

    count = 0
    while count < len(records):
        print(f"Product: {records[count][1]}, Supplier: {records[count][4]}, Supplier Location: {records[count][8]}, {records[count][9]}")
        count = count + 1


def display_missing_products():
    cursor.execute("""
    SELECT * FROM supplier s
    LEFT OUTER JOIN product p
    ON s.supplier_id = p.product_id
    """)

    records = cursor.fetchall()
    print("The suppliers for each product are as follows: ")

    count = 0
    while count < len(records):
        print(f"Supplier: {records[count][1]}, Product: {records[count][5]}")
        count = count + 1