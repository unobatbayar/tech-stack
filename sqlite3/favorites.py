import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        favourite = row["problem"]
        print(favourite)