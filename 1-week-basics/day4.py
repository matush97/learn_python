def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_max(numbers):
    return max(numbers)


def filter_users(users):
    return [user for user in users if user["age"] >= 18]


def count_active_users(users):
    return sum(1 for user in users if user["active"])


def get_user_by_name(users, name):
    for user in users:
        if user["name"] == name:
            return user
    return None