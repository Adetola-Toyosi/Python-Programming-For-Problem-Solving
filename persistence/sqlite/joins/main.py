import database as db

def menu():
    print("""
    Please select one of the following options:
    [1] Display stock levels
    [2] Display suppliers
    [3] Display supplier location
    [4] Display missing suppliers
    [5] Display missing products
        """)

    selection = int(input("Your Selection: \n"))

    if selection == 1:
        db.display_products_with_stock_levels()
    elif selection == 2:
        db.display_product_supplier()
    elif selection == 3:
        db.display_product_supplier_locations()
    elif selection == 4:
        db.display_products_missing_suppliers()
    elif selection == 5:
        db.display_missing_products()




def run():
    menu()

run()