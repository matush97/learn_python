# nacitat data

import csv

total_spending = 0

with open("users_csv.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        total_spending += int(row["amount"])

print("Total spending: ", total_spending)

