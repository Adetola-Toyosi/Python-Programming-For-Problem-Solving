numbers = int(input("How many numbers should i sum up?\n"))
print()

count = 0
total = 0
while count < numbers:
    count = count + 1
    request = int(input(f"Please enter number {count} of {numbers}: \n"))
    total = total + request

print(f"The answer is {total}.")