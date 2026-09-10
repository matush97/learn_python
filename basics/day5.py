import json

from day4 import get_user_by_name, count_active_users, filter_users

with open("../users.json") as file:
    users = json.load(file)

user_by_name = get_user_by_name(users, "Peter")

print("Pouzivatel podla mena: ", user_by_name)
print("Aktivni users : ", count_active_users(users))

users_over_18 = filter_users(users)
print("Starsi ako 18 : ", users_over_18)


json_str = json.dumps(users_over_18)
with open("../sample.json", "w") as f:
    f.write(json_str)
