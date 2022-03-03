def pattern():
    sequences = {}
    sequences["Short Sequence"] = 3
    sequences["Medium Sequence"] = 2
    sequences["Long Sequence"] = 1

    return sequences

def display_keys(data):
    for key in data.keys():
        print(key)

def display_values(data):
    for value in data.values():
        print(value)

def display_items(data):
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    data = pattern()
    print("Dictionary: ")
    print(pattern())
    print()
    display_keys(data)
    print()
    display_values(data)
    print()
    display_items(data)

run()