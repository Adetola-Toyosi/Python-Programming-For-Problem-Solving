import csv

file_path = "../songs.csv"
dest_file_path = "output.csv"
with open(file_path, 'r') as file1:
    with open(dest_file_path, 'w') as file2:
        csv_reader = csv.reader(file1)
        headings = next(csv_reader)
        store = f"{headings[3]}, {headings[2]}, {headings[1]}, {headings[0]}"

        file2.write(str(store))

        for values in csv_reader:
            file2.write(f"\n{str(values[3])}, {str(values[2])}, {str(values[1])}, {str(values[0])}")

print()
