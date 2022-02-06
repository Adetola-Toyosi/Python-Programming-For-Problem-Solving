adventure = str(input("What type of adventure should i have?\n"))
print()

if (adventure == "short") or (adventure == "scary"):
    print("Entering the dark forest!")
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route")
else:
    print("Not sure which route to take.")

