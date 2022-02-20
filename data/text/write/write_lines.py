lines = ["This is the first line.\n", "This is the second.\n", "This is the third line.\n"]

file_path = input("Enter a file path: \n") or "output1.txt"
try:
    if file_path == "":
        with open(file_path, 'w') as file:
            file.writelines(lines)
except IOError:
    print("Please enter a valid file")
