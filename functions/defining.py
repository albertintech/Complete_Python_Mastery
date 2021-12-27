# pylint: disable=invalid-name, missing-docstring

def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")


def get_greeting(name):
    return f"Hi {name}"


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


def save_user(**user):
    print(user)


greet("Albert", "Ramos")
print(get_greeting("Bob"))
print(multiply(2, 3, 4, 5))
save_user(id=1, name="Albert", age=43)
