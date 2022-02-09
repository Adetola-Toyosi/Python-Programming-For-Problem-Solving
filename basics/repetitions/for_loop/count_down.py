distance = int(input("How far are we from the cave?\n"))
print()

for count in range(0, distance, 1):
    print(f"{distance} steps remaining")
    distance = distance - 1

print()
print("We have reached the cave!")