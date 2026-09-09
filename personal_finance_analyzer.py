import csv

total_spending = 0
spending = dict()


def category_spending(user):
    if spending.get(user["category"]):
        amount = int(user["amount"]) + int(spending.get(user["category"]))
        spending.update(({user["category"]: amount}))
    else:
        spending.update(({user["category"]: int(user["amount"])}))


with open("users_csv.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        total_spending += int(row["amount"])
        category_spending(row)

print("Total spending: ", total_spending)
print("\n")

for item in spending:
  print(item.capitalize() + ": " + str(spending[item]))

print("\n")

highest_expense = max(spending, key=spending.get)
print("Highest expense: ", highest_expense.capitalize())

values = spending.values()
avg = sum(values) / len(values)
print("Average transaction: ", avg)
