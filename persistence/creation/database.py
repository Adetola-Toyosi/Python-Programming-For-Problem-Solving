import main

print("Please select one of the following options: ")

entry = int(input("""
    [1] Display a list of all presenters with their organisation
    [2] Display a list of events with their locations
    [3] Display a list of presenters for a specified event
    [4] Display a list of all events for a specific presenter \n
"""))
print()

if entry == 1:
    main.presenters_with_organisation()
elif entry == 2:
    main.events_with_their_location()