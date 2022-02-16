def identify():
    word = input("What lies before us?\n")
    if word == "a large boulder":
        print()
        return "It's time to run!"
    else:
        print()
        return "We'll be fine"

print(identify())
