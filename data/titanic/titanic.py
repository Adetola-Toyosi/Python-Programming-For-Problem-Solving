import csv

file_path = "titanic.csv"
records = []

print("Loading data...", end="")

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)
    # print(headings)

    for values in csv_reader:
        records.append(values)
    print("Done!")
    print(f"Successfully loaded {len(records)} records")