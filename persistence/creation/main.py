import sqlite3 as sql

db = sql.connect('events.db')
cursor = db.cursor()

def presenters_with_organisation():
    """To display a list of presenters with their organisations"""
    cursor.execute("""
    SELECT * FROM presenter p
    INNER JOIN organisation o
    ON p.org_id = o.id
    """)

    records = cursor.fetchall()
    print("List of presenters with their organisations: ")

    for record in records:
        print(f"Presenter: {record[1]}, Organisation: {record[4]}")

