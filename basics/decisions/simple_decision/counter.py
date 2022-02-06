# sets the counters for the even numbers and odd numbers
count_even = 0
count_odd = 0

# reads numbers
first_number = int(input("Please enter the first whole number.\n"))
second_number = int(input("Please enter the second number.\n"))
third_number = int(input("Please enter the third whole number.\n"))

# first number
if first_number % 2 == 0:
    count_even = count_even + 1
else:
    count_odd = count_odd + 1

# second number
if second_number % 2 == 0:
    count_even = count_even + 1
else:
    count_odd = count_odd + 1

# third number
if third_number % 2 == 0:
    count_even = count_even + 1
else:
    count_odd = count_odd + 1

print(f"There were {count_even} even and {count_odd} odd numbers.")

