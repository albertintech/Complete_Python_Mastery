# pylint: disable=invalid-name, missing-docstring

def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")


def get_greeting(name):
    return f"Hi {name}"


greet("Albert", "Ramos")
print(get_greeting("Bob"))
