print("Program Started!")
character = input("Please enter a standard character: \n")

if len(character) == 1:
    value = ord(character)
    print(f"The ASCII code for {character} is: {value}.")
else:
    print("Error, Enter a character")
print("Program Ended!")