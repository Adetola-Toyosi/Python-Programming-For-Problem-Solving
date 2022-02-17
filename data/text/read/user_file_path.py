file_path = input("Enter a file path: \n")

try:
    with open (file_path) as file:
        print(file.readlines())
except IOError:
    print("Sorry, file cannot be displayed.")

