import csv

file_path = "titanic.csv"
records = []

print("Loading data...", end="")  #the 'end' parameter means the next print statement would not be on a new line

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)
    # print(headings)

    for values in csv_reader:
        records.append(values)
    print("Done!")
    print(f"Successfully loaded {len(records)} records")

option = int(input(
"""
Please select one of the following options:
[1] Display names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passenger per age group
\n"""))
print(f"You have selected option: {option}")

def passengers_name():
    print("The names of the passengers are...")
    for record in records:
        names = record[3]
        print(names)
# passengers_name()

def number_of_survivors():
    survived = 0
    not_survived = 0
    for record in records:
        if int(record[1]) == 1:
            survived = survived + 1
        else:
            not_survived = not_survived + 1
    print(f"{survived} passengers survived")
# number_of_survivors()

def nonsurvivors():
    survived = 0
    not_survived = 0
    for record in records:
        if int(record[1]) == 1:
            survived = survived + 1
        else:
            not_survived = not_survived + 1
    print(f"{not_survived} passengers did not survive")
# nonsurvivors()

