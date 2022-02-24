import csv

file_path = "../songs.csv"
dest_file_path = "output.csv"
with open(file_path) as file1:
    with open(dest_file_path, 'w') as file2:
        csv_reader = csv.reader(file1)
        headings = next(csv_reader)
        file2.write(str(headings))

        for values in csv_reader:
            file2.write(f"\n{str(values)}")
