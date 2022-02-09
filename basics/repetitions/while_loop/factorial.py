number = int(input("Please enter a number? \n"))
print()

count = 0
total = 1
while count < number:
    count = count + 1
    total = total * count
print(f"The factorial is {total}")