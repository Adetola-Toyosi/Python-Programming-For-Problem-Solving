import csv

file_path = "user_entries.csv"

with open(file_path, 'w') as file:
    file.write("Year,Artist,Song Title")

    year = int(input("Enter the year the song was produced: "))
    artist = input("Enter the name of the artist: ")
    song_title = input("Enter the song title: ")

    file.write(f"\n{year},{artist},{song_title}")
