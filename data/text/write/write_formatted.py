file_path = input("Enter a file path: \n") or "output2.txt"

lines = ["This is the first line.", "This is the second.", "This is the third line."]

try:
    with open(file_path, "w") as file:
        for line in lines:
            file.write(f"{lines} \n")

except IOError:
    print("Please enter a valid file path")