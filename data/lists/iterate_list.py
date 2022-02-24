def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please enter a direction: ")
    lists = directions()

    for index in range(len(lists)):
        way = lists[index]
        print(f"{index}: {way}")

menu()
