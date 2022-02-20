file_path = input("Enter a file path:\n")
default_file_path = "output.txt"

try:
    if file_path == "":
        with open(default_file_path, "w") as file1:
            file1.write("Data has been overwritten!")
    else:
        with open(file_path, "w") as file2:
            file2.write("Data has been overwritten!")
    print("The data has been written into the file")

except IOError:
    print("Please do the right thing")