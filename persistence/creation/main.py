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

def events_with_their_location():
    """To display a list of events with their organisations"""
    cursor.execute("""
    SELECT * FROM events e 
    INNER JOIN location l
    ON e.loc_id = l.id
    """)

    records = cursor.fetchall()
    print("List of events with their locations: ")

    for record in records:
        print(f"Event: {record[1]}, Location: {record[5]},{record[6]}")

def presenter_for_a_specified_event():
    """To display a list of presenters for a specified event"""
    event_id = int(input("Please enter the event id: \n"))
    cursor.execute(f"""
    SELECT * FROM events e 
    WHERE id={event_id}
    INNER JOIN presenter p
    ON e.id = p.id
    """)

    records = cursor.fetchone()

    for record in records:
        print(record)