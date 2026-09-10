# Vytvor program, ktorý má zoznam používateľov a:
#
# vypíše aktívnych
# spočíta ich počet
# nájde používateľa podľa mena

users = [
    {"active": True, "name": "George Orwell"},
    {"active": False, "name": "Andrzej Sapkowski"},
    {"active": True, "name": "Antoine de Saint-Exupéry"}
]

print("Aktivny useri")

length_users = 0
for user in users:
    length_users += 1

    if user["active"]:
        print(user["name"])

print("Pocet users", length_users)

print("Najdi podla mena:")
name = input()

for user in users:
    if user["name"] == name:
        print(user)