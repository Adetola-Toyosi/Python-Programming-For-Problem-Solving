def directions():
    directions = ["Move Forward", "Move Backwards", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction: ")
    direction = directions()

    for index in range(len(direction)):
        print(f"{index}: {direction[index]}")
    index = int(input())
    return direction[index]

def run():
    route = []
    print("Working out escape route...")
    for something in range(5):
        route.append(menu())
    print(f"Escape route: {route}")

run()





