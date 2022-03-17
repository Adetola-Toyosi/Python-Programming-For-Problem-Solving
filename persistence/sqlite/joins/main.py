import database as db

def menu():
    print("""
    Please select one of the following options:
    [1] Display stock levels
    """)

    selection = int(input("Your Selection: \n"))

    if selection == 1:
        db.display_products_with_stock_levels()



def run():
    menu()

run()