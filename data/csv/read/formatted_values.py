import csv

file_path = "../songs.csv"

try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for values in csv_reader:
            print(f"[{values[3]}] {values[0]} (by {values[1]})")
except:
    print("Cannot read file!, Please check again")
