import csv
file_path = "../songs.csv"

try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader) #to print the headings
        print(f"{headings} \n")

        for values in file:
            print(values)

except IOError:
    print("Cannot read file")