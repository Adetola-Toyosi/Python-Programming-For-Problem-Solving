file_path = input("Please enter a file path: \n")
default_file_path = "quotes.txt"

try:
    if file_path == "":
        with open(default_file_path) as file:
            for line in file:
                print(line.strip())
    else:
        with open(file_path) as file:
            for line in file:
                print(line.strip())
except IOError:
    print("Please enter a valid file path")