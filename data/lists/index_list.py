def movements():
    path = ["Move Forward", 10, "Move Backwards", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    store = movements()
    return f"{store[0]} for {store[1]} steps\n{store[2]} for {store[3]} steps\n{store[4]} for {store[5]} steps\n{store[6]} for {store[7]} steps "

print(run())